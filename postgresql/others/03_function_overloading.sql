-- Function that takes an INTEGER
CREATE FUNCTION double_value(val INTEGER) RETURNS INTEGER AS $$
BEGIN
    RETURN val * 2;
END;
$$ LANGUAGE plpgsql;

-- Overloaded function that takes a NUMERIC
CREATE FUNCTION double_value(val NUMERIC) RETURNS NUMERIC AS $$
BEGIN
    RETURN val * 2.0;
END;
$$ LANGUAGE plpgsql;

SELECT double_value(10);  -- Calls the INTEGER version
-- Output: 20

SELECT double_value(10.5);  -- Calls the NUMERIC version
-- Output: 21

DROP FUNCTION double_value(val NUMERIC);
