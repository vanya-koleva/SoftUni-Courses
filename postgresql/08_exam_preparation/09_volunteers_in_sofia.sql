SELECT
    v.name AS volunteers,
    v.phone_number,
    TRIM(v.address, 'Sofia, ')
FROM
    volunteers AS v
JOIN
    volunteers_departments AS vd
ON
    v.department_id = vd.id
WHERE
    vd.department_name = 'Education program assistant'
        AND
    v.address LIKE '%Sofia%'
ORDER BY
    v.name
;
