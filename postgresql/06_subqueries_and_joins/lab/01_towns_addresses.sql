SELECT
	town_id,
	t.name AS town_name,
	a.address_text
FROM
	addresses AS a
JOIN 
	towns AS t
USING
	(town_id)
WHERE
	t.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
	town_id,
	a.address_id
;
