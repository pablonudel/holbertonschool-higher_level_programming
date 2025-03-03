$ cat 4-first_table.sql
-- creates a table called first_table in the current database 
CREATE TABLE if NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
$