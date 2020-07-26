SELECT a.Email
  FROM (SELECT Email, COUNT(Email) cnt FROM Person GROUP BY Email) a
 WHERE cnt > 1