SELECT
    a.FirstName,
    a.LastName,
    b.City,
    b.State
    
FROM Person a
    LEFT JOIN Address b ON a.Personid = b.Personid
