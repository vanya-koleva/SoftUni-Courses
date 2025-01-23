CREATE TABLE clients(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE employees(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	project_id INT
);

CREATE TABLE projects(
		id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
		client_id INT REFERENCES clients(id),
		project_lead_id INT REFERENCES employees(id)
);

ALTER TABLE
	employees
ADD CONSTRAINT 
	fk_employees_projects
		FOREIGN KEY(project_id)
			REFERENCES projects(id)
;
