CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner VARCHAR
) AS
$$
BEGIN
    SELECT
        o.name INTO owner
    FROM
        animals AS a
    JOIN
        owners AS o
    ON
        a.owner_id = o.id
    WHERE
        a.name = animal_name;

    IF owner IS NULL THEN
        owner := 'For adoption';
    END IF;
END;
$$
LANGUAGE plpgsql;

CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish', '');

CALL sp_animals_with_owners_or_not('Hippo', '');


/*
CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner VARCHAR
) AS
$$
BEGIN
    SELECT
        COALESCE(o.name, 'For adoption') INTO owner
    FROM
        animals AS a
    LEFT JOIN
        owners AS o
    ON
        a.owner_id = o.id
    WHERE
        a.name = animal_name;
END;
$$
LANGUAGE plpgsql;
*/

