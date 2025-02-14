SELECT
    i.name AS item_name,
    ROUND(AVG(r.rating), 2) AS average_rating,
    count(*) as total_reviews,
    b.name AS brand_name,
    c.name AS classification_name
FROM 
    reviews AS r
JOIN 
    items AS i
ON 
    r.item_id = i.id
JOIN 
    brands AS b
ON 
    i.brand_id = b.id
JOIN 
    classifications AS c
ON 
    i.classification_id = c.id
GROUP BY
    i.name, 
    b.name, 
    c.name
HAVING 
    count(*) >= 3
ORDER BY 
    average_rating DESC, 
    item_name
LIMIT 3
;
