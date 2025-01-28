# Subqueries and JOINs

## JOINs

-   better than selects with `WHERE` in performance

-   `INNER JOIN` - Default join - combines rows from both tables only when there is a match.

    -   If no match is found, the row is not included in the result set.

-   `LEFT JOIN` - Includes all rows from the left table, even if there are no matches.

    -   If there’s no match, the columns from the right table will contain NULL.

-   `RIGHT JOIN` - Join the right if left is null.

-   `FULL JOIN`(union) - Join everything. Combines rows from both tables, including:

    -   Matches (where rows in both tables meet the condition).
    -   Unmatched rows from the left table.
    -   Unmatched rows from the right table.

-   `CROSS JOIN` - Cartesian product - **every** element from one table with **every** element from the other. Also formed when the join condition is omitted. Not used often.

## Subqueries

-   SELEFT FROM SELECT
-   Example:

```sql
SELECT
    first_name,
    last_name,
    department, salary
FROM
    employees
WHERE
    salary > (
	    SELECT
            AVG(salary)
	    FROM
            employees
	    WHERE
            department = 'Finance'
);
```

## Indices - Speed Retrieval of Rows

-   Indexing a table involves creating a structure on the table that scans and analyzes it, acting as a kind of shortcut for queries.

-   Think of it like a large book with a bookmark: if you're looking for "zebra," you go directly to the letter "Z."
-   Two types of indexes:
    -   **Clustered index**: Sorts values to allow for binary searching.
    -   **Non-clustered index**: Implements a B-tree (Balanced tree), where unique nodes are created, and each node holds a pointer to the corresponding records.
-   While indexes improve **read performance**, they slow down **updates** and **deletes**, and they also consume **additional memory**.
-   Should be used for big tables only.
-   Should NOT be used on columns that contain a high number of NULL values.
-   Syntax:

```sql
CREATE INDEX index_name_idx
ON table_name(first_column, second_column);
```

## Window functions

Calculate across related rows ("window" of rows) without grouping them.

### ROW_NUMBER()

-   Assigns a unique sequential number to each row in the partition, starting at 1. Gives unique numbers.
-   Each row gets a unique rank, even if there are duplicate values.
-   Syntax:

```sql
ROW_NUMBER() OVER (
    [PARTITION BY col]
    [ORDER BY col]
);
```

-   Example:

```sql
SELECT
    name,
    score,
    ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num
FROM
    scores;
```

| name  | score | row_num |
| ----- | ----- | ------- |
| Alice | 95    | 1       |
| Bob   | 95    | 2       |
| Carol | 90    | 3       |

### RANK()

-   Assigns a rank to each row in the partition, starting at 1.
-   Rows with the same value in the order criteria receive the same rank, but the next rank is skipped (gaps occur).

```sql
SELECT
    name,
    score,
    RANK() OVER (ORDER BY score DESC) AS rank
FROM
    scores;
```

| name  | score | rank |
| ----- | ----- | ---- |
| Alice | 95    | 1    |
| Bob   | 95    | 1    |
| Carol | 90    | 3    |

### DENSE_RANK()

-   Assigns a rank to each row, without gaps in the ranking for tied rows.
-   Tied rows receive the same rank, but the next rank is incremented by 1, regardless of the number of tied rows.

```sql
SELECT
	name,
	score,
	DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank
FROM
	scores;
```

| name  | score | dense_rank |
| ----- | ----- | ---------- |
| Alice | 95    | 1          |
| Bob   | 95    | 1          |
| Carol | 90    | 2          |

### Key Differences:

| Function         | Gaps in Ranking | Tied Rows Get Same Rank? | Sequential Across Rows |
| ---------------- | --------------- | ------------------------ | ---------------------- |
| **ROW_NUMBER()** | No              | No                       | Yes                    |
| **RANK()**       | Yes             | Yes                      | No                     |
| **DENSE_RANK()** | No              | Yes                      | No                     |

