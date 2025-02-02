CREATE OR REPLACE PROCEDURE sp_deposit_money(
    account_id INT,
    money_amount NUMERIC
) AS
$$
BEGIN
    UPDATE
        accounts
    SET
        balance = balance + money_amount
    WHERE
        account_id = id;
END;
$$
LANGUAGE plpgsql;
