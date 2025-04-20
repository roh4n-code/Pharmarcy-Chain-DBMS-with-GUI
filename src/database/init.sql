-- Stored procedure to get all pharmacies
DELIMITER //

CREATE PROCEDURE get_pharmacies()
BEGIN
    SELECT ph_name, ph_add, ph_contact 
    FROM pharmacy;
END //

DELIMITER ; 