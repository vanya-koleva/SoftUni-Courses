CREATE TABLE date_time_types (
	timestamp_column TIMESTAMPTZ,
	interval_column INTERVAL
);

INSERT INTO date_time_types
VALUES 
	('2022-12-31 01:00 EST', '2 days'),
	('2022-12-31 01:00 -8', '1 month'),
	('2022-12-31 01:00 Australia/Melbourne', '1 century'),
	(now(), '1 week')
;

SELECT * FROM date_time_types;

SELECT timestamp_column,
	interval_column,
	timestamp_column - interval_column AS new_date
FROM date_time_types
;

SELECT timestamp_column, CAST(timestamp_column AS VARCHAR(10))
FROM date_time_types
;

--PostgreSQL specific shortcut for CAST, won't port
SELECT timestamp_column::VARCHAR(16) 
FROM date_time_types
;
