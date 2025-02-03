SELECT
    a.name,
    t.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY')
FROM
   animals AS a
JOIN
    animal_types AS t
ON t.id = a.animal_type_id
ORDER BY
    name
;
