-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

DELIMITER //
CREATE TRIGGER ResetEmailValidation
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email AND OLD.valid_email = 0 THEN
        SET OLD.valid_email = NEW.valid_email;
    ELSEIF NEW.email <> OLD.email AND OLD.valid_email = 1 THEN
        SET OLD.valid_email = NEW.valid_email;
    END IF;
END;
//
DELIMITER ;
