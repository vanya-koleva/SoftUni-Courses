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

-   We call functions with `SELECT`.

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

