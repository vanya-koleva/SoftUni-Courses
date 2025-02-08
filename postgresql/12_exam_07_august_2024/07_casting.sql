SELECT
    CONCAT(a.first_name, ' ', a.last_name) AS full_name,
    CONCAT(
        LOWER(LEFT(a.first_name, 1)),
        RIGHT(a.last_name, 2),
        LENGTH(a.last_name),
        '@sm-cast.com'
    ) AS email,
    awards
FROM
    actors AS a
LEFT JOIN
    productions_actors AS pa
ON
    a.id = pa.actor_id
WHERE
    production_id IS NULL
ORDER BY
    awards DESC,
    id
;
