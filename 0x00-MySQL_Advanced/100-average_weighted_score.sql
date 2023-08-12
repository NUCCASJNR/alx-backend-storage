-- Average weighted score

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    UPDATE users u
    SET average_score = (SELECT SUM(c.score * p.weight) / SUM(p.weight)
        AS average_score FROM corrections c JOIN projects p ON p.id = c.project_id
        WHERE c.user_id = u.id); 
END $$ 

DELIMITER ;