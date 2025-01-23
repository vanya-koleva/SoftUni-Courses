SELECT
	r.start_point,
	r.end_point,
	c.id AS leader_id,
	CONCAT(first_name, ' ', last_name) AS leader_name
FROM
	campers AS c
JOIN
	routes as r
ON 
	c.id = r.leader_id
;
