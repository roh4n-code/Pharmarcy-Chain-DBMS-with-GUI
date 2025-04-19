delimiter //
create procedure add_ph(in ph_name varchar(50), ph_add varchar(300), ph_contact varchar(20))
begin
INSERT INTO Pharmacy (ph_name, ph_add, ph_contact) VALUES
(ph_name, ph_add, ph_contact);
end //
