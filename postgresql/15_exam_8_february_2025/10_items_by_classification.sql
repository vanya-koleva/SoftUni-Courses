CREATE OR REPLACE FUNCTION udf_classification_items_count(
    classification_name VARCHAR(30)
) RETURNS varchar AS
$$
DECLARE
    items_count INT;
    result varchar;
BEGIN
    SELECT
        count(i.id)
    INTO 
        items_count
    FROM 
        classifications AS c
    JOIN 
        items AS i
    ON 
        c.id = i.classification_id
    WHERE 
        c.name = classification_name
    ;

    result := CASE
        WHEN items_count > 0 THEN 'Found ' || items_count || ' items.'
        ELSE 'No items found.'
    END;

    RETURN result;

END;
$$
LANGUAGE plpgsql;

