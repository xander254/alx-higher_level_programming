--  a script that updates the score of Bob to 10 in the table second_table without using bobs id
UPDATE second_table
set score = 10
WHERE name = 'Bob';
