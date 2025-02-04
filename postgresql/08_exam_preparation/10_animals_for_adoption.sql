SELECT
    a.name,
    EXTRACT('YEAR' FROM a.birthdate) AS birth_year,
    t.animal_type
FROM
    animals AS a
JOIN
    animal_types as t
ON
    a.animal_type_id = t.id
WHERE
    t.animal_type <> 'Birds'
        AND
    AGE('01/01/2022', a.birthdate) < '5 year'
        AND
    a.owner_id IS NULL 
ORDER BY
    a.name
;
