CREATE OR REPLACE FUNCTION fn_function_name(param_name param_type, param_2 type_2)
RETURNS value_type AS
$$
	DECLARE		-- if needed
		variable_name variable_type;
		variable_2 type_2;
	BEGIN
        RETURN
	END
$$
LANGUAGE plpgsql;

SELECT fn_function_name(arg_1, arg_2);
