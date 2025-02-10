SELECT
    i.name AS ingredient_name,
    p.name AS product_name,
    d.name AS distributor_name
FROM
    ingredients AS i
JOIN
    distributors AS d
ON
    i.distributor_id = d.id
JOIN
    products_ingredients AS pri
ON
    i.id = pri.ingredient_id
JOIN
    products AS p
ON
    pri.product_id = p.id
WHERE
    i.name ILIKE '%mustard%'
        AND
    d.country_id = 16
ORDER BY
    product_name
;
