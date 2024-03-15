-- Same score count
SELECT score, COUNT(score) as number FROM second_table GROUP BY score;
