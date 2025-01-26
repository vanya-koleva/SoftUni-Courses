# Subqueries and JOINs

1. JOINs - better than selects with where in pperformance

    - `INNER JOIN` - Default join - combines rows from both tables only when there is a match.

        - If no match is found, the row is not included in the result set.

    - `LEFT JOIN` - Includes all rows from the left table, even if there are no matches.

        - If there’s no match, the columns from the right table will contain NULL.

    - `RIGHT JOIN` - Join the right if left is null.

    - `FULL JOIN`(union) - Join everything. Combines rows from both tables, including:

        - Matches (where rows in both tables meet the condition).
        - Unmatched rows from the left table.
        - Unmatched rows from the right table.

    - `CROSS JOIN` - Cartesian product - **every** element from one table with **every** element from the other. Also formed when the join condition is omitted. Not used often.

2. Subqueries
    - SELEFT FROM SELECT
    - Example:

```sql
SELECT first_name, last_name, department, salary
FROM employees
WHERE salary > (
	SELECT AVG(salary)
	FROM employees
	WHERE department = 'Finance'
)
```

3. Indices - Speed Retrieval of Rows

    - Indexing a table involves creating a structure on the table that scans and analyzes it, acting as a kind of shortcut for queries.

    - Think of it like a large book with a bookmark: if you're looking for "zebra," you go directly to the letter "Z."
    - Two types of indexes:
        - **Clustered index**: Sorts values to allow for binary searching.
        - **Non-clustered index**: Implements a B-tree (Balanced tree), where unique nodes are created, and each node holds a pointer to the corresponding records.
    - While indexes improve **read performance**, they slow down **updates** and **deletes**, and they also consume **additional memory**.
    - Should be used for big tables only.
    - Should NOT be used on columns that contain a high number of NULL values.
    - Syntax:

```sql
CREATE INDEX index_name_idx
ON table_name(first_column, second_column);
```

