delimiter //
create procedure add_ph(in ph_name varchar(50), ph_add varchar(255), ph_contact varchar(30))
begin
INSERT INTO Pharmacy (ph_name, ph_add, ph_contact) VALUES
(ph_name, ph_add, ph_contact);
end //

delimiter //
create procedure add_pc(in pc_name varchar(50), pc_contact varchar(30))
begin
INSERT INTO PharmaCompany (pc_name, pc_contact) VALUES
(pc_name, pc_contact);
end //


delimiter //
create procedure add_pat(in p_name varchar(50), p_add varchar(255), p_age int, p_aadhar varchar(12), p_doc_aid varchar(12))
begin 
INSERT INTO Patient (p_name, p_add, p_age, p_aadhar, p_doc_aid) VALUES
(p_name, p_add, p_age, p_aadhar, p_doc_aid);
end //


delimiter // 
create procedure add_doc(in d_name varchar(50), spec varchar(30), years_of_exp INT, d_aadhar varchar(12))
begin
INSERT INTO Doctor (d_name, spec, years_of_exp, d_aadhar) VALUES
(d_name, spec, years_of_exp , d_aadhar );
end //


delimiter //
create procedure add_presc(pr_date date, p_id varchar(12), d_id varchar(12))
begin
INSERT INTO Prescription (pr_date, p_id, d_id) VALUES
(pr_date, p_id, d_id);
end //


delimiter //
create procedure add_contr(in pc_name varchar(50), start_date date, end_date date, content varchar(500), supervisor varchar(50), ph_name varchar(50))
begin
INSERT INTO Contract (pc_name, start_date, end_date, content, supervisor, ph_name) VALUES
(pc_name, start_date, end_date, content, supervisor, ph_name);
end //


delimiter //
create procedure add_ph_drug(in pc_name varchar(50), trade_name varchar(50), price decimal(5,2), ph_name varchar(50), quantity int)
begin 
INSERT INTO Pharmacy_Drugs (pc_name, trade_name, price, ph_name,quantity) VALUES
(pc_name, trade_name, price, ph_name,quantity);
end //


delimiter //
create procedure add_drug(in pc_name varchar(50), trade_name varchar(50), formula varchar(50))
begin
INSERT INTO Drugs (pc_name, trade_name, formula) VALUES 
(pc_name, trade_name, formula);
end //


delimiter //
create procedure add_presc_drug(in pc_name varchar(50), trade_name varchar(50), pr_no int, quantity int)
begin
INSERT INTO Prescription_Drugs (pc_name, trade_name, pr_no, quantity) VALUES
(pc_name, trade_name, pr_no, quantity);
end //


delimiter //
create procedure update_pc (in pc_nam varchar(50), in pc_contac varchar(30))
begin
update PharmaCompany
set pc_contact = pc_contac
where pc_name = pc_nam;
end //


delimiter //
create procedure update_ph (in ph_nam varchar(50), ph_ad varchar(255), ph_contac varchar(30))
begin
update Pharmacy
set ph_add = ph_ad, ph_contact = ph_contac
where ph_name = ph_nam;
end //


delimiter //
create procedure update_pat(in p_nam varchar(50), p_ad varchar(255), p_ag int, p_aadha varchar(12), p_doc_ai varchar(12))
begin
update Patient
set p_name = p_nam, p_add = p_ad, p_age = p_ag, p_doc_aid = p_doc_ai
where p_aadhar = p_aadha;
end //


delimiter //
create procedure update_doc(in d_nam varchar(50), spe varchar(30), years_of_ex INT, d_aadha varchar(12))
begin
update Doctor
set d_name = d_nam, spec = spe, years_of_exp = years_of_ex
where d_aadhar = d_aadha;
end //


delimiter //
create procedure update_presc(in pr_n int, pr_dat date, p_i varchar(12), d_i varchar(12))
begin
update Prescription 
set pr_date = pr_dat, p_id = p_i, d_id = d_i
where pr_no = pr_n;
end //


delimiter //
create procedure update_contr(in pc_nam varchar(50), start_dat date, end_dat date, conten varchar(500), superviso varchar(50), ph_nam varchar(50))
begin
update Contract
set end_date = end_dat, content = conten, supervisor = superviso
where pc_name = pc_nam and ph_name = ph_nam;
end //


delimiter //
create procedure update_ph_drug(in pc_nam varchar(50), trade_nam varchar(50), pric decimal(5,2), ph_nam varchar(50), quantit int)
begin 
update Pharmacy_Drugs
set price = pric, quantity = quantit
where pc_name = pc_nam and trade_name = trade_nam and ph_name = ph_nam;
end //


delimiter //
create procedure update_drug(in pc_nam varchar(50), trade_nam varchar(50), formul varchar(50))
begin
update Drugs
set pc_name = pc_nam, formula = formul
where trade_name =  trade_nam;
end //


delimiter //
create procedure update_presc_drug(in pc_nam varchar(50), trade_nam varchar(50), pr_n int, quantit int)
begin
update Prescription_Drugs
set quantity= quantit
where pc_name = pc_nam and trade_name = trade_nam and pr_no = pr_n;
end  //


delimiter //
create procedure del_pres_drug(in pc_nam VARCHAR(50), trade_nam VARCHAR(50), pr_n INT)
begin
delete from Prescription_Drugs 
where pc_name = pc_nam and trade_name = trade_nam and pr_no = pr_n;
end //


delimiter //
create procedure del_ph_drug(in trade_nam varchar(50), ph_nam varchar(50))
begin
delete from Pharmacy_Drugs
where ph_name = ph_nam and trade_name = trade_nam;
end//


delimiter //
create procedure del_drug(in trade_nam varchar(50))
begin
delete from Drugs
where trade_name = trade_nam;
end  //


delimiter // 
create procedure del_contr(in pc_nam varchar(50), ph_nam varchar(50))
begin
delete from Contract
where pc_name = pc_nam and ph_name = ph_nam;
end //


delimiter //
create procedure del_presc(pr_dat date, p_i varchar(12), d_i varchar(12))
begin
delete from Prescription
where p_id = p_i and  d_id  = d_i and  pr_date = pr_dat;
end // 


delimiter //
create procedure del_doc(in d_aadha varchar(12))
begin
delete from Doctor
where d_aadhar  =  d_aadha;
end//


delimiter //
create procedure del_pat(in p_aadha varchar(255))
begin 
delete from Patient
where p_aadhar =  p_aadha;
end //


delimiter //
create procedure del_pc(in pc_nam varchar(50))
begin
delete from PharmaCompany
where pc_name = pc_nam;
end //


delimiter //
create procedure del_ph(in ph_nam varchar(50))
begin
delete from Pharmacy
where ph_name = ph_nam;
end //
















