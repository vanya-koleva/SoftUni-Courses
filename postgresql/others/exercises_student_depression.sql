-- https://www.kaggle.com/datasets/hopesb/student-depression-dataset

CREATE TYPE type_sleep_duration 
AS ENUM (
	'Less than 5 hours',
	'5-6 hours',
	'7-8 hours',
	'More than 8 hours',
	'Others'
);

CREATE TYPE type_dietary_habits
AS ENUM (
	'Healthy',
	'Moderate',
	'Unhealthy',
	'Others'
);

CREATE TYPE type_yes_no
AS ENUM (
	'Yes',
	'No'
);

CREATE TABLE st_depression (
	id INT PRIMARY KEY,
	gender VARCHAR(20),
	age NUMERIC(3, 1),
	city VARCHAR(50),
	profession VARCHAR(50),
	academic_pressure NUMERIC(2, 1),
	work_pressure NUMERIC(2, 1),
	cgpa NUMERIC(4, 2),  --Grade Point Average or other academic scores
	study_satisfaction NUMERIC(2, 1),
	job_satisfaction NUMERIC(2, 1),
	sleep_duration type_sleep_duration,  --Average daily sleep duration
	dietary_habits type_dietary_habits,
	degree VARCHAR(50),
	ever_had_suicidal_thoughts type_yes_no,
	work_study_hours NUMERIC(3, 1),
	financial_stress NUMERIC(4, 2),
	family_history_of_mental_illness type_yes_no,
	depression BOOL
);

/*
Through the terminal:
docker ps
docker cp /path/to/your/file.csv <container_name>:/file.csv
docker exec -it <container_name> bash
psql -U <username> -d <database_name>
COPY your_table_name
FROM '/file.csv'
DELIMITER ','
CSV HEADER;
*/

DROP TABLE st_depression;
DROP TYPE type_sleep_duration;
DROP TYPE type_dietary_habits;
DROP TYPE type_yes_no;

SELECT * FROM st_depression
;

SELECT DISTINCT work_study_hours
FROM st_depression
ORDER BY work_study_hours DESC
;

SELECT DISTINCT ON (degree) degree, financial_stress
FROM st_depression
;

SELECT DISTINCT degree, financial_stress
FROM st_depression
;

SELECT *
FROM st_depression
WHERE financial_stress IS NULL
;

SELECT financial_stress
FROM st_depression
ORDER BY financial_stress DESC
;

SELECT dietary_habits, depression
FROM st_depression
WHERE dietary_habits NOT IN ('Healthy', 'Moderate')
ORDER BY dietary_habits DESC
;

SELECT age, study_satisfaction, depression
FROM st_depression
WHERE age BETWEEN 20.0 AND 30.0 AND depression = true
ORDER BY study_satisfaction DESC
;

SELECT
	CONCAT(
		gender,
		', ',
		age
	) AS student,
	CONCAT_WS(
		', ',
		city,
		degree, 
		profession
	) AS information,
	depression,
	ever_had_suicidal_thoughts AS "suicidal thoughts"
FROM
	st_depression AS d
WHERE
	ever_had_suicidal_thoughts = 'Yes' 
		AND 
	city ILIKE '%Jai%'
LIMIT 10
;

ALTER TABLE 
	st_depression
RENAME TO 
	students
;

ALTER TABLE 
	students
RENAME COLUMN 
	ever_had_suicidal_thoughts 
TO 
	suicidal_thoughts
;

SELECT DISTINCT 	--All columns are used to determine uniqueness. Completely unique rows
	city,
	academic_pressure
FROM
	students
ORDER BY
	city
LIMIT 10
;

SELECT DISTINCT ON (city) 	--Applies only to specified column(s). Unique rows based on certain columns
	city,
	academic_pressure
FROM
	students
ORDER BY
	city
LIMIT 10
;

SELECT DISTINCT ON (city, academic_pressure)
	city,
	academic_pressure
FROM
	students
ORDER BY
	city
LIMIT 10
;
