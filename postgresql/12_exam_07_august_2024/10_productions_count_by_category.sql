CREATE OR REPLACE FUNCTION udf_category_productions_count(
    category_name VARCHAR(50)
) RETURNS VARCHAR AS
$$
DECLARE
    productions_count INT;
BEGIN
    SELECT
        COUNT(production_id)
    INTO
        productions_count
    FROM
        categories_productions
    WHERE
        category_id = (
            SELECT
                id
            FROM
                categories
            WHERE
                name = category_name
        );

    RETURN CONCAT('Found ', productions_count, ' productions.');
END;
$$
LANGUAGE plpgsql;
