delete P1
from Person P1
inner join Person P2
where P1.id > P2.id 
and P1.email = P2.email
