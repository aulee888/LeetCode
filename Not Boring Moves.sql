SELECT *
FROM cinema
WHERE (id % 2 = 1) 
    AND description NOT IN ('boring')
GROUP BY rating DESC
