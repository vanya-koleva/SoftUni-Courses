SELECT
	b.booking_id,
	c.first_name AS customer_name
FROM
-- same as CROSS JOIN
	bookings AS b,
	customers AS c
ORDER BY
	customer_name
;
