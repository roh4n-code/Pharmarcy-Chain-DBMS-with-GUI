USE pharmadb;

-- Basic CRUD procedures
DELIMITER //
CREATE PROCEDURE add_ph(IN ph_name VARCHAR(50), ph_add VARCHAR(255), ph_contact VARCHAR(30))
BEGIN
    INSERT INTO Pharmacy (ph_name, ph_add, ph_contact) VALUES
    (ph_name, ph_add, ph_contact);
END //

DELIMITER //
CREATE PROCEDURE add_pc(IN pc_name VARCHAR(50), pc_contact VARCHAR(30))
BEGIN
    INSERT INTO PharmaCompany (pc_name, pc_contact) VALUES
    (pc_name, pc_contact);
END //

DELIMITER //
CREATE PROCEDURE add_pat(IN p_name VARCHAR(50), p_add VARCHAR(255), p_age INT, p_aadhar VARCHAR(12), p_doc_aid VARCHAR(12))
BEGIN 
    INSERT INTO Patient (p_name, p_add, p_age, p_aadhar, p_doc_aid) VALUES
    (p_name, p_add, p_age, p_aadhar, p_doc_aid);
END //

DELIMITER // 
CREATE PROCEDURE add_doc(IN d_name VARCHAR(50), spec VARCHAR(30), years_of_exp INT, d_aadhar VARCHAR(12))
BEGIN
    INSERT INTO Doctor (d_name, spec, years_of_exp, d_aadhar) VALUES
    (d_name, spec, years_of_exp, d_aadhar);
END //

DELIMITER //
CREATE PROCEDURE add_presc(pr_date DATE, p_id VARCHAR(12), d_id VARCHAR(12))
BEGIN
    INSERT INTO Prescription (pr_date, p_id, d_id) VALUES
    (pr_date, p_id, d_id);
END //

DELIMITER //
CREATE PROCEDURE add_contr(IN pc_name VARCHAR(50), start_date DATE, end_date DATE, content VARCHAR(500), supervisor VARCHAR(50), ph_name VARCHAR(50))
BEGIN
    INSERT INTO Contract (pc_name, start_date, end_date, content, supervisor, ph_name) VALUES
    (pc_name, start_date, end_date, content, supervisor, ph_name);
END //

DELIMITER //
CREATE PROCEDURE add_ph_drug(IN pc_name VARCHAR(50), trade_name VARCHAR(50), price DECIMAL(5,2), ph_name VARCHAR(50), quantity INT)
BEGIN 
    INSERT INTO Pharmacy_Drugs (pc_name, trade_name, price, ph_name, quantity) VALUES
    (pc_name, trade_name, price, ph_name, quantity);
END //

DELIMITER //
CREATE PROCEDURE add_drug(IN pc_name VARCHAR(50), trade_name VARCHAR(50), formula VARCHAR(50))
BEGIN
    INSERT INTO Drugs (pc_name, trade_name, formula) VALUES 
    (pc_name, trade_name, formula);
END //

DELIMITER //
CREATE PROCEDURE add_presc_drug(IN pc_name VARCHAR(50), trade_name VARCHAR(50), pr_no INT, quantity INT)
BEGIN
    INSERT INTO Prescription_Drugs (pc_name, trade_name, pr_no, quantity) VALUES
    (pc_name, trade_name, pr_no, quantity);
END //

-- Update procedures
DELIMITER //
CREATE PROCEDURE update_pc(IN pc_nam VARCHAR(50), IN pc_contac VARCHAR(30))
BEGIN
    UPDATE PharmaCompany
    SET pc_contact = pc_contac
    WHERE pc_name = pc_nam;
END //

DELIMITER //
CREATE PROCEDURE update_ph(IN ph_nam VARCHAR(50), ph_ad VARCHAR(255), ph_contac VARCHAR(30))
BEGIN
    UPDATE Pharmacy
    SET ph_add = ph_ad, ph_contact = ph_contac
    WHERE ph_name = ph_nam;
END //

DELIMITER //
CREATE PROCEDURE update_pat(IN p_nam VARCHAR(50), p_ad VARCHAR(255), p_ag INT, p_aadha VARCHAR(12), p_doc_ai VARCHAR(12))
BEGIN
    UPDATE Patient
    SET p_name = p_nam, p_add = p_ad, p_age = p_ag, p_doc_aid = p_doc_ai
    WHERE p_aadhar = p_aadha;
END //

DELIMITER //
CREATE PROCEDURE update_doc(IN d_nam VARCHAR(50), spe VARCHAR(30), years_of_ex INT, d_aadha VARCHAR(12))
BEGIN
    UPDATE Doctor
    SET d_name = d_nam, spec = spe, years_of_exp = years_of_ex
    WHERE d_aadhar = d_aadha;
END //

DELIMITER //
CREATE PROCEDURE update_presc(IN pr_n INT, pr_dat DATE, p_i VARCHAR(12), d_i VARCHAR(12))
BEGIN
    UPDATE Prescription 
    SET pr_date = pr_dat, p_id = p_i, d_id = d_i
    WHERE pr_no = pr_n;
END //

DELIMITER //
CREATE PROCEDURE update_contr(IN pc_nam VARCHAR(50), start_dat DATE, end_dat DATE, conten VARCHAR(500), superviso VARCHAR(50), ph_nam VARCHAR(50))
BEGIN
    UPDATE Contract
    SET end_date = end_dat, content = conten, supervisor = superviso
    WHERE pc_name = pc_nam AND ph_name = ph_nam;
END //

DELIMITER //
CREATE PROCEDURE update_ph_drug(IN pc_nam VARCHAR(50), trade_nam VARCHAR(50), pric DECIMAL(5,2), ph_nam VARCHAR(50), quantit INT)
BEGIN 
    UPDATE Pharmacy_Drugs
    SET price = pric, quantity = quantit
    WHERE pc_name = pc_nam AND trade_name = trade_nam AND ph_name = ph_nam;
END //

DELIMITER //
CREATE PROCEDURE update_drug(IN pc_nam VARCHAR(50), trade_nam VARCHAR(50), formul VARCHAR(50))
BEGIN
    UPDATE Drugs
    SET pc_name = pc_nam, formula = formul
    WHERE trade_name = trade_nam and pc_name = pc_nam;
END //

DELIMITER //
CREATE PROCEDURE update_presc_drug(IN pc_nam VARCHAR(50), trade_nam VARCHAR(50), pr_n INT, quantit INT)
BEGIN
    UPDATE Prescription_Drugs
    SET quantity = quantit
    WHERE pc_name = pc_nam AND trade_name = trade_nam AND pr_no = pr_n;
END //

-- Delete procedures
DELIMITER //
CREATE PROCEDURE del_pres_drug(IN pc_nam VARCHAR(50), trade_nam VARCHAR(50), pr_n INT)
BEGIN
    DELETE FROM Prescription_Drugs 
    WHERE pc_name = pc_nam AND trade_name = trade_nam AND pr_no = pr_n;
END //

DELIMITER //
CREATE PROCEDURE del_ph_drug(IN trade_nam VARCHAR(50), ph_nam VARCHAR(50))
BEGIN
    DELETE FROM Pharmacy_Drugs
    WHERE ph_name = ph_nam AND trade_name = trade_nam;
END //

DELIMITER //
CREATE PROCEDURE del_drug(IN trade_nam VARCHAR(50),IN pc_nam VARCHAR(50))
BEGIN
    DELETE FROM Drugs
    WHERE trade_name = trade_nam AND pc_name = pc_nam;
END //

DELIMITER // 
CREATE PROCEDURE del_contr(IN pc_nam VARCHAR(50), ph_nam VARCHAR(50))
BEGIN
    DELETE FROM Contract
    WHERE pc_name = pc_nam AND ph_name = ph_nam;
END //

-- FIXED: Updated to take prescription ID instead of date, patient ID and doctor ID
DELIMITER //
CREATE PROCEDURE del_presc(IN pr_id INT)
BEGIN
    DELETE FROM Prescription
    WHERE pr_no = pr_id;
END //

DELIMITER //
CREATE PROCEDURE del_doc(IN d_aadha VARCHAR(12))
BEGIN
    DELETE FROM Doctor
    WHERE d_aadhar = d_aadha;
END //

DELIMITER //
CREATE PROCEDURE del_pat(IN p_aadha VARCHAR(12))
BEGIN 
    DELETE FROM Patient
    WHERE p_aadhar = p_aadha;
END //

DELIMITER //
CREATE PROCEDURE del_pc(IN pc_nam VARCHAR(50))
BEGIN
    DELETE FROM PharmaCompany
    WHERE pc_name = pc_nam;
END //

DELIMITER //
CREATE PROCEDURE del_ph(IN ph_nam VARCHAR(50))
BEGIN
    DELETE FROM Pharmacy
    WHERE ph_name = ph_nam;
END //

-- Report procedures
DELIMITER //
CREATE PROCEDURE p_report(IN p_aadhar VARCHAR(12), IN s_dat DATE, IN e_dat DATE)
BEGIN
    SELECT pr.pr_no, d.d_name, pr.pr_date
    FROM Prescription pr
    JOIN Patient p ON p.p_aadhar = pr.p_id
    JOIN Doctor d ON d.d_aadhar = pr.d_id
    WHERE p_id = p_aadhar AND s_dat <= pr_date AND pr_date <= e_dat;
END //
    
DELIMITER // 
CREATE PROCEDURE pr_details(IN p_aadhar VARCHAR(12), IN pr_dat DATE)
BEGIN
    SELECT d.d_name, pd.pc_name, pd.trade_name, pd.quantity 
    FROM Prescription pr
    INNER JOIN Prescription_Drugs pd ON pr.pr_no = pd.pr_no
    JOIN Doctor d ON pr.d_id = d.d_aadhar
    WHERE pr.p_id = p_aadhar AND pr.pr_date = pr_dat;
END //

DELIMITER // 
CREATE PROCEDURE pc_production(IN pc_nam VARCHAR(50))
BEGIN
    SELECT trade_name, formula 
    FROM Drugs
    WHERE pc_name = pc_nam;
END //

DELIMITER // 
CREATE PROCEDURE ph_stock(IN ph_nam VARCHAR(50))
BEGIN
    SELECT pc_name, trade_name, price, quantity
    FROM Pharmacy_Drugs
    WHERE ph_name = ph_nam;
END //

DELIMITER //
CREATE PROCEDURE pch_con(IN pc_nam VARCHAR(50), IN ph_nam VARCHAR(50))
BEGIN
    SELECT * 
    FROM Contract
    WHERE ph_name = ph_nam AND pc_name = pc_nam;
END //

-- View procedures
DELIMITER //
CREATE PROCEDURE p_view()
BEGIN
    SELECT p_name, p_aadhar
    FROM Patient;
END //

DELIMITER //
CREATE PROCEDURE d_view()
BEGIN
    SELECT d_name, d_aadhar, years_of_exp, spec
    FROM Doctor;
END //

DELIMITER //
CREATE PROCEDURE d_patient(IN d_aadhar VARCHAR(12))
BEGIN
    SELECT p.p_name, p.p_add, p.p_age, p.p_aadhar 
    FROM Patient p
    JOIN Doctor d ON d.d_aadhar = p.p_doc_aid
    WHERE d_aadhar = p.p_doc_aid;
END //

-- Get data procedures
DELIMITER //
CREATE PROCEDURE get_pharmacies()
BEGIN
    SELECT ph_name, ph_add, ph_contact
    FROM Pharmacy;
END //

DELIMITER //
CREATE PROCEDURE get_companies()
BEGIN
    SELECT pc_name, pc_contact
    FROM PharmaCompany;
END //

DELIMITER //
CREATE PROCEDURE get_patients_full()
BEGIN
    SELECT p.p_name, p.p_add, p.p_age, p.p_aadhar, p.p_doc_aid, d.d_name
    FROM Patient p
    LEFT JOIN Doctor d ON p.p_doc_aid = d.d_aadhar;
END //

DELIMITER //
CREATE PROCEDURE get_prescriptions()
BEGIN
    SELECT pr.pr_no, pr.pr_date, p.p_name, d.d_name,
        p.p_aadhar AS p_id, d.d_aadhar AS d_id
    FROM Prescription pr
    JOIN Patient p ON pr.p_id = p.p_aadhar
    JOIN Doctor d ON pr.d_id = d.d_aadhar
    ORDER BY pr.pr_date DESC;
END //

DELIMITER //
CREATE PROCEDURE get_prescription_drugs(IN prescription_id INT)
BEGIN
    SELECT pd.pc_name, pd.trade_name, pd.quantity
    FROM Prescription_Drugs pd
    WHERE pd.pr_no = prescription_id;
END //

DROP PROCEDURE IF EXISTS get_patient_prescriptions;
DELIMITER //
CREATE PROCEDURE get_patient_prescriptions(IN patient_id VARCHAR(12))
BEGIN
    SELECT pr.pr_no, pr.pr_date, d.d_name as doctor_name
    FROM Prescription pr
    JOIN Doctor d ON pr.d_id = d.d_aadhar
    WHERE pr.p_id = patient_id
    ORDER BY pr.pr_date DESC;
END //

DELIMITER //
CREATE PROCEDURE get_contracts()
BEGIN
    SELECT 
        c.pc_name, c.ph_name, c.supervisor, 
        c.start_date, c.end_date, c.content,
        pc.pc_contact as company_contact,
        ph.ph_contact as pharmacy_contact
    FROM Contract c
    JOIN PharmaCompany pc ON c.pc_name = pc.pc_name
    JOIN Pharmacy ph ON c.ph_name = ph.ph_name
    ORDER BY c.pc_name, c.ph_name;
END //

DELIMITER // 
CREATE PROCEDURE get_drugs()
    BEGIN
        SELECT *
        FROM Drugs;
    END //