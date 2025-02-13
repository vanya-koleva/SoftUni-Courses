SELECT
    first_name,
    last_name,
    salary
FROM
    employees
WHERE
    salary > (
        SELECT
            salary
        FROM
            employees
        WHERE
            last_name = 'Bull'
    )
;

SELECT
    first_name,
    last_name
FROM
    employees
WHERE
    department_id IN (
        SELECT
            department_id
        FROM
            departments
        WHERE
            department_name = 'IT'
    )
;

SELECT
    first_name,
    last_name,
FROM
    employees
WHERE manager_id IN (
        SELECT 
            employee_id
        FROM 
            employees 
        WHERE 
            department_id IN (
                SELECT 
                    department_id 
                FROM 
                    departments 
                WHERE 
                    location_id IN (
                        SELECT 
                            location_id
                        FROM 
                            locations 
                        WHERE 
                            country_id = 'US'
                    )
            )
    )
;

