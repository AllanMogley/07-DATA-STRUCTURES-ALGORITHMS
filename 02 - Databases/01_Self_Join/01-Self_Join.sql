# Write your MySQL query statement below
# Create a copy of table then make selections

SELECT e2.name as Employee FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE e1.salary < e2.salary
