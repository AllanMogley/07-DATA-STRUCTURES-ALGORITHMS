select p.firstName, p.lastNameId, a.city, a.state from Person as p left join Address as a on p.personId = a.personId
