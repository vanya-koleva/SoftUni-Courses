CREATE OR REPLACE PROCEDURE udp_modify_account(
    address_street VARCHAR(30),
    address_town VARCHAR(30)
) AS
$$
DECLARE
    searched_id INT;
BEGIN
    SELECT
        account_id
    INTO
        searched_id
    FROM
        addresses
    WHERE
        street = address_street
            AND
        town = address_town;

    UPDATE
        accounts
    SET
        job_title = CONCAT('(Remote) ', job_title)
    WHERE
        id = searched_id;
END;
$$
LANGUAGE plpgsql;

