# Table Relations

## Steps in Database Design

1. Identification of the entities.

-   The term "entity" refers to a real-world object or concept that is represented in the database. For example, in a library system, entities might include _books, authors_, and _borrowers_. Each of these entities is represented by a table in the database.
-   Each table represents an object that is important to the busines.
-   Identify the main entities in the system based on the requirements. Most often they are nouns in the specification. We should start building a dictionary by initiating conversations with experts in the field.
-   Create a table for each entity to store its relevant data.
-   Ensure that the table corresponds directly to the object it represents, making the design intuitive and aligned with the real-world structure

2. Defining table columns.

-   The attributes of the entities.
-   It is a good practice to include additional columns, such as a column that stores the creation date of a record, who created it, etc.

3. Defining primary keys (PK).

-   Always define an additional column for the primary key.
    -   Don't use an existing column.
    -   Do not use business terms as a Primary Key because, no matter how much the business assures us that something is unique and will always remain so, it should not be trusted.
    -   Must be declared as a PRIMARY KEY.
    -   Put the primary key in the first column. - Exceptions:
        -   Entities that have well-known ID, e.g., countries (BG, DE, US) and currencies (USD, EUR, BGN).
-   IDs are either INT or STRING.
-   It is more secure to use strings because they are harder to crack with brute force.
-   Integers are efficient for indexing and querying.
-   If something is a PK, it is inherently unique.

4. Modeling relationships.

-   By using relationships, we avoid repeating data in the database.
-   Define a foreign key:

    ```sql
    CREATE TABLE clients (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30)
    );

    CREATE TABLE orders (
        id SERIAL PRIMARY KEY,
        client_id INT REFERENCES clients
    );
    ```

-   Define a foreign key using the foreign key constraint:

    ```sql
    CREATE TABLE orders (
        id INT PRIMARY KEY,
        client_id INT,
        CONSTRAINT fk_client
            FOREIGN KEY(client_id)
                REFERENCES clients(id)
    );
    ```

-   Many-to-One: A relationship where multiple records in one table are associated with a single record in another table.
-   Many-to-Many: Achieved using a junction/mapping table.  
    Implementation:

    ```sql
    CREATE TABLE employees(
        id SERIAL PRIMARY KEY,
        employee_name VARCHAR(50)
    );

    CREATE TABLE projects(
        id SERIAL PRIMARY KEY,
        project_name VARCHAR(50)
    );

    CREATE TABLE employees_projects(    -- Mapping table
        employee_id INT,
        project_id INT,
        CONSTRAINT pk_employees_projects
            PRIMARY KEY(employee_id, project_id),
        CONSTRAINT fk_employees_projects_employees
            FOREIGN KEY(employee_id)
            REFERENCES employees(id),
        CONSTRAINT fk_employees_projects_projects
            FOREIGN KEY(project_id)
            REFERENCES projects(id)
    );
    ```

-   Composite Key: A key made up of multiple columns, such as concat(f_name, l_name) to create a unique identifier from first and last name.
-   One-to-One: A relationship where a record in one table is linked to exactly one record in another table. Used rarely.

5. Defining constraints.
6. Filling test data.

## Table Design Principles

1. No data duplication.
2. Unique identifiers.
3. NULL values only where necessary.
4. Integration of references.
5. Atomic data – data is broken into small parts. For example, storing first_name and last_name separately to allow separate access.
6. Selection of appropriate data.
7. Indexing.
8. Access control.

## JOINs

-   With JOINS we can get data from two tables simultaneously by pointing a "join condition".

```sql
SELECT * FROM table_a
    JOIN table_b ON
        table_b.common_column = table_a.common_column;
```

## CASCADE DELETE

-   When deleting a record that is related to others through a relationship, cascade delete ensures that all related records are also deleted.  
    Example: Deleting a customer from the Customers table also deletes all their orders from the Orders table.

-   Use Cascade Delete to maintain data consistency, especially if dependent records cannot exist without the parent record.

-   Do not use Cascade Delete if you need to preserve historical data or logs (e.g., order history for a deleted customer).
-   CASCADE can be either DELETE or UPDATE

## CASCADE UPDATE:

-   Avoid it. Using triggers or procedures instead of cascade updates offers more explicit control and can handle complex update scenarios effectively, reducing the risk of unintended consequences.

-   When to Use:

    -   If the primary key is not set to auto-increment, meaning it can be modified.
    -   Ideal when combined with the UNIQUE constraint.

-   Do not use it if the primary key is auto-incremented.

## Relational Schema

-   The structural blueprint of a database that comprises of:

    -   The schemas of all individual tables.
    -   The relationships between these tables.
    -   Other database objects such as constraints.

-   Does not contain data, but metadata

-   Relational schemas are graphically displayed in Entity
    / Relationship diagrams (E/R Diagrams)

## Atomic data

-   One value per cell.
-   Atomic data refers to information that is indivisible and cannot be further broken down into smaller meaningful parts. This type of data represents the smallest unit of meaningful data in a given context, often treated as a single, self-contained value.

    -   Like a single LEGO brick—simple, small, and whole all by itself.

-   Atomic data is crucial in database design and other structured data systems, particularly for:
    -   Normalization: Ensuring that database tables are structured in a way that avoids redundancy and allows easy updates.
    -   Clarity: Atomic data improves readability and prevents ambiguity.
    -   Scalability: It facilitates easier data manipulation, querying, and integration.

