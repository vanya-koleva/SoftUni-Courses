SELECT
    p.id,
    p.title,
    pri.duration,
    ROUND(pri.budget, 1) AS budget,
    TO_CHAR(pri.release_date, 'MM-YY') AS release_date
FROM
    productions AS p
JOIN
    productions_info AS pri
ON
    p.production_info_id = pri.id
WHERE
    EXTRACT(YEAR FROM release_date) IN (2023, 2024)
        AND
    budget > 1500000.00
ORDER BY
    budget,
    duration DESC,
    id
LIMIT 3
;
