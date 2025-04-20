delimiter //
CREATE PROCEDURE p_report(IN p_aadhar varchar(12), IN s_dat date, IN e_dat date)
	begin
	SELECT pr.pr_no, d.d_name, pr.pr_date
	FROM Prescription pr
    JOIN Patient p ON p.p_aadhar = pr.p_id
    JOIN Doctor d ON d.d_aadhar = pr.d_id
	WHERE p_id = p_aadhar AND s_dat <= pr_date AND pr_date <= e_dat;
	end//
    
delimiter // 
CREATE PROCEDURE pr_details(IN p_aadhar varchar(12),IN pr_dat date)
	begin
	SELECT d.d_name, pd.pc_name, pd.trade_name, pd.quantity 
	FROM Prescription pr
    INNER JOIN Prescription_Drugs pd ON pr.pr_no = pd.pr_no
	JOIN Doctor d ON pr.d_id = d.d_aadhar
    WHERE pr.p_id = p_aadhar AND pr.pr_date = pr_dat;
	end//

delimiter // 
CREATE PROCEDURE pc_production(IN pc_nam varchar(50))
	begin
	SELECT trade_name,formula 
	FROM Drugs
	WHERE pc_name = pc_nam;
	end//

delimiter // 
CREATE PROCEDURE ph_stock(IN ph_nam varchar(50))
	begin
	SELECT pc_name,trade_name,price,quantity
	FROM pharmacy_drugs
	WHERE ph_name = ph_nam;
	end//

delimiter //
CREATE PROCEDURE pch_con(IN pc_nam varchar(50),IN ph_nam varchar(50))
	begin
	SELECT * 
	FROM contract
	WHERE ph_name = ph_nam AND pc_name = pc_nam;
	end//

delimiter //
CREATE PROCEDURE p_view()
	begin
    SELECT p_name,p_aadhar
    FROM Patient;
    end//

delimiter //
CREATE PROCEDURE d_view()
	begin
    SELECT d_name,d_aadhar,spec
    FROM Doctor;
    end//

delimiter //
CREATE PROCEDURE d_patient(IN d_aadhar varchar(12))
	begin
	SELECT p.p_name,p.p_add,p.p_age,p.p_aadhar 
	FROM Patient p
    JOIN Doctor d on d.d_aadhar = p.p_doc_aid
	WHERE d_aadhar= p.p_doc_aid;
	end//

delimiter //
CREATE PROCEDURE get_pharmacies()
    begin
    SELECT ph_name, ph_add, ph_contact
    FROM Pharmacy;
    end//

delimiter //
CREATE PROCEDURE get_companies()
    begin
    SELECT pc_name, pc_contact
    FROM PharmaCompany;
    end//

delimiter //
CREATE PROCEDURE get_patients_full()
    begin
    SELECT p.p_name, p.p_add, p.p_age, p.p_aadhar, p.p_doc_aid, d.d_name
    FROM Patient p
    LEFT JOIN Doctor d ON p.p_doc_aid = d.d_aadhar;
    end//

delimiter //
CREATE PROCEDURE get_prescriptions()
    begin
    SELECT pr.pr_no, pr.pr_date, p.p_name, d.d_name,
           p.p_aadhar as p_id, d.d_aadhar as d_id
    FROM Prescription pr
    JOIN Patient p ON pr.p_id = p.p_aadhar
    JOIN Doctor d ON pr.d_id = d.d_aadhar
    ORDER BY pr.pr_date DESC;
    end//

delimiter //
CREATE PROCEDURE get_prescription_drugs(IN prescription_id INT)
    begin
    SELECT pd.pc_name, pd.trade_name, pd.quantity
    FROM Prescription_Drugs pd
    WHERE pd.pr_no = prescription_id;
    end//
