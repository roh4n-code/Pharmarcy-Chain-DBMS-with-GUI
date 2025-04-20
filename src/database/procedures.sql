-- Procedure to view all pharmacies
DELIMITER //
CREATE PROCEDURE ph_view()
BEGIN
    SELECT ph_name, ph_add, ph_contact 
    FROM pharmacy;
END //

-- Procedure to view all companies
DELIMITER //
CREATE PROCEDURE pch_con()
BEGIN
    SELECT pc_name, pc_contact
    FROM pharm_comp;
END //

-- Procedure to view company production (already exists)
-- CREATE PROCEDURE pc_production(IN company_name VARCHAR(255))
-- BEGIN
--     SELECT * FROM drug WHERE pc_name = company_name;
-- END //

DELIMITER ; 