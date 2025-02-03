SELECT
    CONCAT(o.name, ' - ', a.name),
    o.phone_number,
    ac.cage_id
FROM
    owners AS o
JOIN
    animals AS a
ON
    o.id = a.owner_id
JOIN
    animals_cages AS ac
ON
    a.id = ac.animal_id
JOIN
    animal_types AS t
ON
    a.animal_type_id = t.id
WHERE
    t.animal_type = 'Mammals'
ORDER BY
    o.name,
    a.name DESC
;
