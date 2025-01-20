# DATA AGGREGATION

-   Aggregation refers to the process of combining multiple individual elements into a single group or whole.
-   Data aggregation is the process of gathering, organizing, and summarizing raw data from various sources to produce meaningful and concise information.

## Grouping

-   Treating same records as one.
-   GROUP BY can be used with aggregate functions (unlike DISTINCT).
> [!IMPORTANT]  
> It is mandatory to group by all the columns we have selected (except for the aggregate functions).

## Aggregate Functions

-   Perform operations on multiple rows to return a single result.
-   The aggregate functions are **used only with SELECT**.
-   MIN, MAX, AVG, COUNT, SUM
-   They usually **ignore NULL values**.
-   COUNT(column) - Returns the number of rows in the given column.
-   COUNT(DISTINCT column) - Returns the number of unique non-null values in the group
-   COUNT(\*) - Counts primary keys

## Having

-   Only with aggregations
-   Places conditions on groups
-   Done after the data is processed

### Differences Between WHERE and HAVING

-   `WHERE` - A filter for the logic - "Do this on..."

    -   Filters the data **before it is grouped**.
    -   Operates on individual rows.
    -   Cannot use aggregate functions (e.g., SUM, COUNT) because it applies to rows before grouping (aggregation).

-   `HAVING` - A filter for the presentattion - "Show me..."
    -   Filters groups **after grouping**.
    -   Operates on aggregated results (e.g., SUM, AVG).
    -   Requires aggregate functions.

## CASE

-   The same as if-else statement.
-   If there is no ELSE when none of the conditions is met, it returns NULL.

-   General syntax (recommended):

```sql
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ...
ELSE result_n
END AS column_name
```

-   Simple syntax (not recommended):

```sql
CASE expression
    WHEN value_1 THEN result_1
    WHEN value_2 THEN result_2
    ...
ELSE result_n
END AS column_name
```

---

-   Syntax order:

```sql
SELECT ...
FROM ...
WHERE...
GROUP BY...
HAVING...
ORDER BY...
```

