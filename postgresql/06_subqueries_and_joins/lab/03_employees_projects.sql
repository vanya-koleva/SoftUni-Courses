SELECT
	employee_id,
	CONCAT(e.first_name, ' ', e.last_name),
	project_id,
	p.name AS project_name
FROM
	employees AS e
JOIN
	employees_projects AS ep
USING
	(employee_id)
JOIN
	projects AS p
USING
	(project_id)
WHERE
	project_id = 1
;

