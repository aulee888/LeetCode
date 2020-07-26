SELECT class 
  FROM (SELECT DISTINCT * FROM courses) a 
 GROUP BY class 
HAVING COUNT(class) >= 5 