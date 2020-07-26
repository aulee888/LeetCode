SELECT a.Id Id 
  FROM weather a
       JOIN weather b ON DATEDIFF(a.RecordDate, b.RecordDate) = 1 AND a.Temperature > b.Temperature