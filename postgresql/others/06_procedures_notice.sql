CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10,2) NOT NULL
);

INSERT INTO employees (name, salary) VALUES
('Alice Johnson', 60000.00),
('Bob Smith', 75000.00),
('Charlie Davis', 50000.00),
('Diana White', 90000.00);

SELECT * FROM employees;

CREATE PROCEDURE get_employee_details(
    IN emp_id INT,
    OUT emp_name TEXT,
    OUT emp_salary NUMERIC
)
AS $$
BEGIN
    SELECT name, salary
    INTO emp_name, emp_salary
    FROM employees
    WHERE id = emp_id;
END;
$$ LANGUAGE plpgsql;

CALL get_employee_details(2, NULL, NULL);

CREATE PROCEDURE get_employee_status(
    IN emp_id INT,
    OUT emp_name TEXT,
    OUT status_message TEXT
)
AS $$
BEGIN
    -- Try to get the employee's name
    SELECT name INTO emp_name
    FROM employees
    WHERE id = emp_id;

    -- Check if employee exists
    IF emp_name IS NOT NULL THEN
        status_message := 'Success: Employee found';
    ELSE
        status_message := 'Failure: No employee found with the given ID';
    END IF;
END;
$$ LANGUAGE plpgsql;

CALL get_employee_status(2, NULL, NULL);

CREATE OR REPLACE PROCEDURE update_employee_salary(emp_id INT, new_salary NUMERIC)
LANGUAGE plpgsql
AS $$
DECLARE
    current_salary NUMERIC;
BEGIN
    -- Fetch current salary
    SELECT salary INTO current_salary
    FROM employees
    WHERE id = emp_id;

    -- Check if employee exists
    IF FOUND THEN
        -- Update salary
        UPDATE employees SET salary = new_salary WHERE id = emp_id;

        -- Display success message
        RAISE NOTICE 'Salary updated successfully for Employee ID: %, Old Salary: %, New Salary: %',
            emp_id, current_salary, new_salary;
    ELSE
        -- Employee not found
        RAISE NOTICE 'Employee ID % not found. No update performed.', emp_id;
    END IF;
END;
$$;

CALL update_employee_salary(1, 40000.00);

SELECT * FROM employees WHERE id = 1;
