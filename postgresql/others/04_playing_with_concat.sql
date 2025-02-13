CREATE TABLE countries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    country_name VARCHAR(50)
);

CREATE TABLE persons(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country_id INT REFERENCES countries
);

INSERT INTO countries (country_name)
VALUES
    ('USA'),
    ('Canada'),
    ('Mexico');

INSERT INTO persons (first_name, last_name, country_id)
VALUES
    ('John', 'Doe', 1),
    ('Jane', 'Smith', 2),
    ('Carlos', 'Hernandez', 3),
    (NULL, 'Smith', 2),
    ('Anna', NULL, 1),
    (NULL, NULL, 3);

CREATE OR REPLACE FUNCTION fn_get_persons()
RETURNS TABLE(id INT, full_name TEXT, country VARCHAR)
AS
$$
    BEGIN
        RETURN QUERY(
            SELECT
                p.id,
                -- CONCAT returns TEXT
                CONCAT(p.first_name, ' ', p.last_name),
                c.country_name
            FROM
                persons AS p
            JOIN
                countries c
    ON
                p.country_id = c.id
        );
    END
$$
LANGUAGE plpgsql;

--Error, cannot change return type
CREATE OR REPLACE FUNCTION fn_get_persons()
RETURNS TABLE(id INT, full_name VARCHAR, country VARCHAR)
AS
$$
    BEGIN
        RETURN QUERY(
            SELECT
                p.id,
                (p.first_name || ' ' || p.last_name) :: VARCHAR,
                c.country_name
            FROM
                persons AS p
            JOIN
                countries c
    ON
                p.country_id = c.id
        );
    END
$$
LANGUAGE plpgsql;

DROP FUNCTION fn_get_persons();

SELECT * FROM fn_get_persons();

SELECT fn_get_persons();

SELECT
     CONCAT(first_name, ' ', last_name)
FROM
    persons;

SELECT
    first_name || last_name
FROM
    persons;

TRUNCATE TABLE persons;
