-- a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name IF name EXISTS
FROM second_table
ORDER BY DESC;
