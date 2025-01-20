CREATE TABLE IF NOT EXISTS dates  (
	start_date DATE,
	end_date DATE,
	interval_column INTERVAL,
	next_end_date TIMESTAMPTZ
	);

INSERT INTO 
    dates (start_date, end_date)
SELECT 
    (DATE '2024-01-01' + (random() * 364)::INT) AS start_date,
    (DATE '2025-01-01' + (random() * 364)::INT) AS end_date
FROM generate_series(1, 50)
;

UPDATE 
	dates
SET
    interval_column = (end_date - start_date) * INTERVAL '1 day'
;

UPDATE
	dates
SET
	next_end_date = end_date + interval_column
;

SELECT * FROM dates;
