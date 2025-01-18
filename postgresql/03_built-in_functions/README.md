# BUILT-IN FUNCTIONS

## String Functions

-   SUBSTRING(string, start_pos, length: optional) - String from Position for Length - Returns part of string from start_pos with **length** (not last index). Can be used to check if a string is a substring of another string.
-   SUBSTRING(input_string, pattern_string) - If pattern_string was found in input string it will be returned, else return null.
-   SUBSTRING(input_string, regex) - If regex was found in input string it will be returned, else return null.

-   LEFT, RIGHT(string, count) - Get characters from the beginning or the end of a string.

    -   LEFT with negative n gives all characters except the **LAST** n.
    -   RIGHT with negative n gives all characters except the **FIRST** n.

-   REPLACE(string, pattern, replacement) - case sensitive – Replaces all occurrences.

-   TRIM(string, char) – Deletes all occurrences of the symbol until it finds a different symbol then the provided one.

    -   LTRIM(string, char)
    -   RTRIM(string, char)

-   LENGTH(string)
-   CHAR_LENGTH(string) – same as LENGTH;
-   BIT_LENGTH – EVERY symbol from the ascii table is 8 bytes, others depend on the encoding

-   LOWER, UPPER, (string)

-   REVERSE(string)

-   REPEAT(string, count)

-   INSERT(String, Position, chars count to delete, sub string)

-   TRANSLATE(string, pattern, code) -> will replace in string char from pattern with same possition char from code

-   CAST(variable AS data_type) -> cast variable to data_type.

    -   :: is another way to cast.  
        :: is postges specific, CAST is SQL standart

-   POSITION(pattern IN string) - return the position(index) of the pattern in a string. Returns 0 if no pattern found.
    ```sql
    SELECT POSITION('sub' IN 'This is a substring example') AS position; -- 11
    ```

## Math Functions

-   /, -, \*, +, %, ^ - power, |/ - square root, @ - abs
    АBS()
    PI
    ```sql
    SELECT PI() AS pi_value;
    ```
-   SQRT(number)
-   POW (number, power)

-   ROUND(number, decimal_place) - UP >= 5 DOWN 4 <=
-   TRUNC(float, decimal_place) - cut float to decimal_place after point. No Rounding up or down. If no decimal_place return integer without rounding up or down.
-   FLOOR, CEIL

-   SIGN(number) - returns the sign of a given numeric value. It outputs:  
     1 if the number is positive,  
     -1 if the number is negative,  
     0 if the number is zero.

-   RANDOM() - generates a random value between 0 (inclusive) and 1 (exclusive).  
    Number between 0 and 6:

```sql
SELECT CEIL(RANDOM() * 100) % 7 AS random_mod_7;
```

## Date Functions

-   EXTRACT (part FROM DATE) - PART - YEAR, MONTH, DAY, MINUTES…  
    e.g.: extract('YEAR" FROM DATE)

-   AGE(first_date, second_date) - find the difference between two dates. It subtracts the second argument from the first one and returns an interval as a result. Example:  
    AGE(died, born) AS "Life Span"

-   TO_CHAR(date, format) - formats the date according to the format
    -   TO_CHAR(NOW() AT TIME ZONE 'UTC', 'YYYY-MM-DD HH24:MI:SS TZD');  
        Result: '2023-09-20 12:34:56 UTC'
-   TO_CHAR(data) -> convert data to a string

To see all time zones:

```sql
SELECT * FROM pg_timezone_names;
```

To see current date/time:

```sql
SELECT CURRENT_DATE;  -- 2025-01-18
SELECT CURRENT_TIME;  --13:46:17.495425+00:00
SELECT NOW();  -- 2025-01-18 13:47:36.195425+00:00
SELECT CURRENT_TIMESTAMP; -- 2025-01-18 14:25:33.306674+00
```

## WILD_CARDS

-   expression LIKE pattern - similar to regex - match text values against a pattern, based on whether something starts/ends on a pattern

    -   % - 0 or more characters
    -   \_ - any single character, exact position  
        LIKE – case-sensitive  
        ILIKE - case-insensitive

-   ESCAPE – specify a prefix to treat special characters as normal.  
    WHERE last*name LIKE '%l!*%' ESCAPE '!';

-   REGEXP_MATCH(string, pattern [, flags])
-   REGEXP_REPLACE(string, pattern, replacement [, flags])

```sql
SELECT regexp_replace('abc123xyz', '\d+', '456');
-- Output: abc456xyz
```

With `g` flag:

```sql
SELECT regexp_replace('abc123xyz456', '\d+', '456', 'g');
-- Output: abc456xyz456
```

