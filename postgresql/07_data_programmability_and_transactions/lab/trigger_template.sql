CREATE FUNCTION trigger_fn_function_name()
RETURNS TRIGGER
AS
$$
BEGIN
	RETURN NULL; -- NULL/OLD/NEW
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_trigger_name
AFTER DELETE 	--BEFORE/AFTER INSERT/UPDATE/DELETE
[OF column_name] ON the_table_name
FOR EACH ROW 	-- FOR EACH ROW / FOR EACH STATEMENT
[WHEN (condition)]
EXECUTE PROCEDURE 	-- EXECUTE FUNCTION works in later PostgreSQL versions
trigger_fn_function_name();
