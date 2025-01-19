# DATA AGGREGATION

-   Aggregation refers to the process of combining multiple individual elements into a single group or whole.
-   Data aggregation is the process of gathering, organizing, and summarizing raw data from various sources to produce meaningful and concise information.

## Grouping

-   Treating same records as one
-   GROUP BY can be used with aggregate functions (unlike DISTINCT)

## Aggregate Functions

-   MIN, MAX, AVG, COUNT, SUM
-   They usually **ignore NULL values**.
-   COUNT(column) - Counts all rows in the given column.
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

Syntax order:  
```sql
SELECT ...
FROM ...
WHERE...
GROUP BY...
HAVING...
ORDER BY...
```

