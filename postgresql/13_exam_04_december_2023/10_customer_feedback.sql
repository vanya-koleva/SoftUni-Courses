CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(
    product_name VARCHAR(25)
) RETURNS TABLE(
    customer_id INT,
    customer_name VARCHAR(75),
    feedback_description VARCHAR(255),
    feedback_rate NUMERIC(4, 2)
) AS
$$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        f.description,
        f.rate
    FROM
        customers AS c
    JOIN
        feedbacks AS f
    ON
        c.id = f.customer_id
    WHERE
        f.product_id IN (
            SELECT
                id
            FROM
                products
            WHERE
                name = product_name
        )
    ORDER BY
        c.id
    ;
END;
$$
LANGUAGE plpgsql;
