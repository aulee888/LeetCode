SELECT a.Score, b.Rank 
  FROM Scores a, (SELECT Score, RANK() OVER(ORDER BY Score DESC) `Rank` 
                    FROM Scores 
                    GROUP BY Score) b 
 WHERE a.Score = b.Score 
 ORDER BY a.Score DESC