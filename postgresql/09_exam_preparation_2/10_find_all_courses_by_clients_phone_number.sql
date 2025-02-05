CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT AS
$$
DECLARE
    courses_number INT;
BEGIN
    SELECT
        COUNT(co.id) 
    INTO 
        courses_number
    FROM
        clients AS cl
    JOIN
        courses AS co
    ON
        cl.id = co.client_id
    WHERE
        cl.phone_number = phone_num;

    RETURN courses_number;
END;
$$
LANGUAGE plpgsql;

SELECT fn_courses_by_client('(803) 6386812');
