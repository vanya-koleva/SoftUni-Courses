SELECT
	CONCAT(surname, ', ', firstname) AS name
FROM
	cd.members
;

SELECT
	facid,
	name,
	membercost,
	guestcost,
	initialoutlay,
	monthlymaintenance
FROM
	cd.facilities
WHERE
	name LIKE 'Tennis%'
;

SELECT
	facid,
	name,
	membercost,
	guestcost,
	initialoutlay,
	monthlymaintenance
FROM
	cd.facilities
WHERE
	name ILIKE 'tennis%'
;

SELECT
	memid,
	telephone
FROM
	cd.members
WHERE
	telephone ~ '[()]'
ORDER BY
	memid
;

SELECT
	LPAD(zipcode::TEXT, 5, '0') AS zip
FROM
	cd.members
ORDER BY 
	zip
;
