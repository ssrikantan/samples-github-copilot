-- Declare a variable to store the name of the table
DECLARE
  table_name VARCHAR2(30) := 'EMPLOYEES';

-- Create a table with three columns: ID, NAME, and SALARY
BEGIN
  -- Execute the DDL statement using EXECUTE IMMEDIATE
  EXECUTE IMMEDIATE 'CREATE TABLE ' || table_name || ' (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50) NOT NULL,
    SALARY NUMBER(10,2) CHECK (SALARY > 0)
  )';
  
  -- Insert some data into the table using a loop
  FOR i IN 1..10 LOOP
    -- Generate some random values for name and salary
    EXECUTE IMMEDIATE 'INSERT INTO ' || table_name || ' VALUES (
      :id,
      :name,
      :salary
    )' USING i, 'Employee ' || i, ROUND(DBMS_RANDOM.VALUE(1000, 10000), 2);
  END LOOP;
  
  -- Commit the changes
  COMMIT;
END;
/

-- Declare a cursor to query the table
DECLARE
  -- Define the cursor with a SELECT statement
  CURSOR emp_cur IS
    SELECT * FROM EMPLOYEES ORDER BY SALARY DESC;
    
  -- Declare a record variable to store each row fetched by the cursor
  emp_rec emp_cur%ROWTYPE;
BEGIN
  -- Open the cursor
  OPEN emp_cur;
  
  -- Loop through the cursor until no more rows are found
  LOOP
    -- Fetch the next row from the cursor into the record variable
    FETCH emp_cur INTO emp_rec;
    
    -- Exit the loop if no more rows are found
    EXIT WHEN emp_cur%NOTFOUND;
    
    -- Display the data from the record variable
    DBMS_OUTPUT.PUT_LINE('ID: ' || emp_rec.id || ', NAME: ' || emp_rec.name || ', SALARY: ' || emp_rec.salary);
  END LOOP;
  
  -- Close the cursor
  CLOSE emp_cur;
END;
/
