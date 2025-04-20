-- Stored procedure to get all pharmacies
DELIMITER //

CREATE PROCEDURE get_pharmacies()
BEGIN
    SELECT ph_name, ph_add, ph_contact 
    FROM pharmacy;
END //

DELIMITER ;

DROP PROCEDURE IF EXISTS del_presc;
DELIMITER //
CREATE PROCEDURE del_presc(IN pr_id INT)
BEGIN
    DELETE FROM Prescription
    WHERE pr_no = pr_id;
END //
DELIMITER ;