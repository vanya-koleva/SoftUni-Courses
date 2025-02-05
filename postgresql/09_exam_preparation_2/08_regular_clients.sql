SELECT
    cl.full_name,
    COUNT(co.car_id) AS count_of_cars,
    SUM(bill)
FROM
    clients AS cl
JOIN
    courses AS co
ON
    cl.id = co.client_id
WHERE
    full_name LIKE '_a%'
GROUP BY
    cl.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    full_name
;
