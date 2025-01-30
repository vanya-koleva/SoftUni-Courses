DROP FUNCTION log_items CASCADE;

CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	status INT,
	created DATE DEFAULT now()
);

CREATE TABLE items_log(
	id SERIAL PRIMARY KEY,
	status INT,
	created DATE DEFAULT now()
);

CREATE FUNCTION log_items()
RETURNS TRIGGER AS 
$$
	BEGIN
		INSERT INTO items_log (id, status, created)
		VALUES (new.id, new.status, new.created);
		RETURN new;
	END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER log_items_trigger
AFTER INSERT ON items
FOR EACH ROW EXECUTE PROCEDURE log_items()
;

CREATE OR REPLACE FUNCTION delete_last_items_log()
RETURNS TRIGGER 
AS
$$
	BEGIN
		WHILE (SELECT COUNT(*) FROM items_log) > 8 LOOP
			DELETE FROM items_log WHERE id = (SELECT MIN(id) FROM items_log);
		END LOOP;
		RETURN NEW;
	END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER clear_items_log_trigger
AFTER INSERT ON items_log   
FOR EACH STATEMENT EXECUTE PROCEDURE delete_last_items_log()
;

INSERT INTO items (id, status)
VALUES
	(1, FLOOR(RANDOM() * 100)),
	(2, FLOOR(RANDOM() * 100)),
	(3, FLOOR(RANDOM() * 100)),
	(4, FLOOR(RANDOM() * 100)),
	(5, FLOOR(RANDOM() * 100)),
	(6, FLOOR(RANDOM() * 100))
;

INSERT INTO items (id, status)
VALUES
	(7, FLOOR(RANDOM() * 100)),
	(8, FLOOR(RANDOM() * 100)),
	(9, FLOOR(RANDOM() * 100)),
	(10, FLOOR(RANDOM() * 100)),
	(11, FLOOR(RANDOM() * 100)),
	(12, FLOOR(RANDOM() * 100))
;

SELECT * FROM items_log;

SELECT * FROM items;
