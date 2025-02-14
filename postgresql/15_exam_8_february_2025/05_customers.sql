SELECT
    id,
    last_name,
    loyalty_card
FROM
    customers
WHERE
    last_name ILIKE '%m%'
        AND
    loyalty_card = TRUE
ORDER BY 
    last_name DESC, id
;

