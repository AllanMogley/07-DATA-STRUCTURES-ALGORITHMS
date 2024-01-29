-- Write your PostgreSQL query statement below
select firstname, lastname, city, state from person
left join Address 
on Person.personId = Address.personId

-- select the required columns
-- Do a left join
-- Left join to keep all records from the person table 
