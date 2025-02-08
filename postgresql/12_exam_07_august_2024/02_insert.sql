INSERT INTO
    actors(first_name, last_name, birthdate, height, awards, country_id)
SELECT
    REVERSE(first_name),
    REVERSE(last_name),
    birthdate - 2 days,
    CASE
        WHEN height IS NOT NULL THEN height + 10
        ELSE 10
    END,
    country_id,
    (SELECT
         id
     FROM
         countries
     WHERE
         name = 'Armenia'
    )
FROM
    actors
WHERE
    id BETWEEN 10 AND 20
;
