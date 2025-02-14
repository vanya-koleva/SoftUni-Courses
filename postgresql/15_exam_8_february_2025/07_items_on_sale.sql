SELECT
    i.name,
    concat(upper(b.name), '/', lower(c.name)) AS promotion,
    concat('On sale: ', i.description),
    i.quantity
FROM 
    items AS i
JOIN 
    brands AS b
ON 
    i.brand_id = b.id
JOIN 
    classifications AS c
ON 
    i.classification_id = c.id
WHERE 
    i.id NOT IN (
        SELECT 
            item_id
        FROM 
            orders_items
    )
ORDER BY 
    quantity DESC, 
    name
;
