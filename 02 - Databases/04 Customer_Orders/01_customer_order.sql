select c.id as 'Customers' from customers c
left join orders o
on c.id = o.customersId
where o.id is null
