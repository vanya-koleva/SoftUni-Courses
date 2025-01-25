SELECT
	a.name,
	a.country,
	CAST(b.booked_at AS DATE) AS booked_at
FROM
	apartments AS a
LEFT JOIN
	bookings AS b
USING
	(booking_id)
LIMIT 10
;
