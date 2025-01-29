CREATE TABLE bank(
	id INT PRIMARY KEY,
	name VARCHAR(20),
	bgn INT
);

INSERT INTO
	bank(id, name, bgn)
VALUES
	(1, 'Ivan', 1000),
	(2, 'Mimi', 2000)
;

CREATE OR REPLACE PROCEDURE sp_transfer_money(
	IN sender_id INT,
	IN receiver_id INT,
	IN transfer_amount INT,
	OUT status VARCHAR(50)
)
AS
$$
	DECLARE
		sender_amount INT;
		receiver_amount INT;
		temp_val INT;
	BEGIN
		SELECT bgn FROM bank WHERE id = sender_id INTO sender_amount;
		IF sender_amount < transfer_amount THEN
			status := 'The sender does not have enough money';
			RETURN;
		END IF;
		SELECT bgn FROM bank WHERE id = receiver_id INTO receiver_amount;

		UPDATE bank SET bgn = bgn + transfer_amount WHERE id = receiver_id;
		UPDATE bank SET bgn = bgn - transfer_amount WHERE id = sender_id;

		SELECT bgn FROM bank WHERE id = sender_id INTO temp_val;
		IF sender_amount - transfer_amount <> temp_val THEN
			status := 'Error when transferring from sender';
			ROLLBACK;
			RETURN;
		END IF;

		SELECT bgn FROM bank WHERE id = receiver_id INTO temp_val;
		IF receiver_amount + transfer_amount <> temp_val THEN
			status := 'Error when transferring to receiver';
			ROLLBACK;
			RETURN;
		END IF;

		status := 'Success';
		COMMIT;
	END
$$
LANGUAGE plpgsql
;

CALL sp_transfer_money(1, 2, 1200, '')
;

CALL sp_transfer_money(1, 2, 900, '')
;

SELECT * FROM bank
;
