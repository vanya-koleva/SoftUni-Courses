CREATE PROCEDURE sp_procedure_name(param_1)
AS 
$$
DECLARE auxiliary_value_if_needed value_type
RAISE NOTICE 'Message: %', some_value; -- good to have, not mundatory
END 
$$
LANGUAGE plpgsql;

CALL sp_procedure_name(arg_1);
