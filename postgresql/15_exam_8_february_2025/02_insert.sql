INSERT INTO
    items(name, quantity, price, description, brand_id, classification_id)
SELECT
    concat('Item', r.created_at),
    r.customer_id,
    r.rating * 5,
    NULL,
    r.item_id,
    (SELECT
         rv.item_id
     FROM
         reviews AS rv
     ORDER BY
         rv.item_id
     LIMIT 1
    )
FROM
    reviews AS r
ORDER BY
    r.item_id
LIMIT 10
;
