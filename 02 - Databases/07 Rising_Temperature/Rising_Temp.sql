select d1.id from Weather d1, Weather d2
where datediff(d1.recordDate, d2.recordDate) = 1
and d1.temperature > d2.temperature
