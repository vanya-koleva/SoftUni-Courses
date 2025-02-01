# Database Programmability

## Functions

-   Used to **return a value**, not to modify tables. They can do the latter but it is not recommended.
-   Creating a function:

    -   The function can be written in different languages: Python, Pascal, plpgsql.

    -   We specify the **return type**.

    -   Created in 'routines' folder in DataGrip.

-   Functions in PostgreSQL are categorized into three types:

    -   **STABLE** – These functions return the same result for the same table state, e.g., a function that counts rows.
    -   **IMMUTABLE** – The function always returns the same result, independent of tables, e.g., squaring a number.
    -   **VOLATILE** – These are the default functions, which may change (e.g., using variables).

-   Defining a function as STABLE or IMMUTABLE can improve performance.

-   Variables can be accessed using $number notation, but this is not recommended.

-   We can declare and use variables with `DECLARE`.

-   `RETURNS` - Specifies the type of value that will be returned.

-   `RETURN` - Returns a value.

-   **plpgsql** - Procedural Language/PostgreSQL:

    -   `:=` - the assignment operator in plpgsql.
    -   `=` - comparison.
    -   Every instruction ends with `;`
    -   Variables are defined with their types before the logic begins.

-   No nested functions, but functions can call other functions.

-   **Function overloading** - We can have functions that have the same name but accept different number (or types) of parameters. In practice, they are different functions.

-   Syntax:

```sql
CREATE FUNCTION fn_function_name(parameters_with_tyes)
RETURNS return_type AS $$
DECLARE
BEGIN
    -- Function logic
    RETURN
END;
$$ LANGUAGE plpgsql;

```

-   When returning a **TABLE**, we must specify the types of the columns. `RETURNS TABLE(columns)...RETURN QUERY...)`

```sql
CREATE FUNCTION get_users()
RETURNS TABLE(id INT, name TEXT) AS $$
BEGIN
    RETURN QUERY SELECT u.id, u.name FROM users AS u;
END;
$$ LANGUAGE plpgsql;
```

-   We call functions with `SELECT`. This means they must return something. Even if you don't need a value, PostgreSQL enforces a return type. `RETURNS void` is used when the function is void.

```sql
SELECT fn_count_employees_by_town('Sofia') AS count;
```

## Procedures

-   In most cases, procedures are **VOID functions** (they do not return a value).

-   Executed using `CALL`.

-   They allow some part of the **logic** to be removed from the application and stored **in the RDBMS**.

    -   This can significantly cut down traffic on the network.

    -   Improve security.

    -   Encapsulate complex operations and logic, making it so other developers do not need to know how the whole DB operates to work with what they need.

-   Can be accessed by programs using different platforms and APIs.

-   Unlike functions, procedures in PostgreSQL are primarily used to **manipulate data**. Another difference is that they do not use RETURN to return values, but they can pass data using OUT parameters if needed.

-   It is best practice for procedures to **communicate their status** (OUT parameters, RAISE NOTICE) to confirm whether they completed successfully.
-   The message from RAISE NOTICE goes in Output, not Result tab.

-   `IN` - Input parameters. These are passed to the procedure when it is called.
-   `OUT` - Output parameters, which are returned to the caller after execution.
-   `INOUT` - Can be used both as input and output (i.e., passed in, modified inside the procedure, and returned). The caller can pass an argument to a function. The function changes the argument and returns the updated value.

```sql
CREATE OR REPLACE FUNCTION sum_avg(
    a NUMERIC,
    b NUMERIC,
    c NUMERIC,
    OUT total NUMERIC,
    OUT avg_value NUMERIC
)
AS $$
BEGIN
    total := a + b + c;
    avg_value := TRUNC(total / 3, 2);
END;
$$ LANGUAGE plpgsql;

SELECT * FROM sum_avg(10, 20, 30);
```

-   `INTO` - store the result of a `SELECT` query into a variable.

-   The := operator is used for **variable assignment**, whereas SELECT ... INTO is used for fetching **query results** into variables.

-   `SQLERRM` - SQL Error Message - Stores the error message of the last encountered exception.

## Transactions

-   Actions that we perform on the database and can roll back if we wish.
-   These actions are executed as a whole - either all of them succeed or fail as a whole.

-   They start with `BEGIN` and end with either `ROLLBACK` or `COMMIT`.

-   All changes within a transaction are temporary. At any time, all changes can be canceled by `ROLLBACK`. Changes persist when `COMMIT` is executed.

```sql
-- Start a transaction
BEGIN;

-- Deduct $100 from Alice's account
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;

-- Add $100 to Bob's account
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Check Bob's new balance
DECLARE
    bob_balance DECIMAL(20,2);
BEGIN
    SELECT balance INTO bob_balance FROM accounts WHERE account_id = 2;
    IF bob_balance > 1000 THEN
        RAISE NOTICE 'Bob has too much money. Rolling back transaction.';
        ROLLBACK;
        RETURN;
    END IF;
END;
```

-   Savepoint Example:

```sql
-- Start the transaction
BEGIN;

-- Add some amount
UPDATE accounts SET balance = balance + 50 WHERE id = 1;

-- Create a savepoint
SAVEPOINT my_savepoint;

-- Deduct some amount
UPDATE accounts SET balance = balance - 30 WHERE id = 1;

-- Decide for some reason to rollback to the savepoint
ROLLBACK TO SAVEPOINT my_savepoint;

END;
```

## Triggers

-   Functions executed **Before/After** a **DELETE/UPDATE/INSERT** query.
-   Similar to event listeners in JS.

```sql
CREATE OR REPLACE FUNCTION update_last_modified()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_modified = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_last_modified
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_last_modified();
```

