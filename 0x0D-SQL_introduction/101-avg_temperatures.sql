-- Import in hbtn_0c_0 database this table dump: download
--Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temperature) AS avg_temperature
FROM tempratures
GROUP BY city
ORDER BY avg_temperature DESC;