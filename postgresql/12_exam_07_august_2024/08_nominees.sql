SELECT
    c.name,
    COUNT(p.id) AS productions_count,
    COALESCE(AVG(pri.budget), 0)
FROM
    countries AS c
JOIN
    productions AS p
ON
    c.id = p.country_id
JOIN
    productions_info AS pri
ON
    p.production_info_id = pri.id
GROUP BY
    c.name
HAVING
    COUNT(p.id) >= 1
ORDER BY
    productions_count DESC,
    c.name
;
