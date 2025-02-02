CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC
) AS
$$
DECLARE
    current_balance NUMERIC;
BEGIN
    current_balance := (SELECT balance FROM accounts WHERE id = account_id);

    IF current_balance >= money_amount THEN
        UPDATE
            accounts
        SET
            balance = balance - money_amount
        WHERE
            account_id = id;
    ELSE
        RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
    END IF;
END;
$$
LANGUAGE plpgsql;
