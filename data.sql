-- Pharmaceutical Companies Data
INSERT INTO PharmaCompany (pc_name, pc_contact) VALUES
('Pfizer', '+1-212-733-2323'),
('Novartis', '+41-61-324-1111'),
('Bayer', '+49-214-30-1'),
('GlaxoSmithKline', '+44-20-8047-5000'),
('Sun Pharma', '+91-22-4324-4324'),
('Johnson & Johnson', '+1-732-524-0400'),
('Sanofi', '+33-1-53-77-40-00'),
('Roche', '+41-61-688-1111'),
('Merck', '+1-908-740-4000'),
('AstraZeneca', '+44-20-7604-8000');

INSERT INTO PharmaCompany (pc_name, pc_contact) VALUES ('Medplus' , '6969696969');


-- Drugs Data
INSERT INTO Drugs (pc_name, trade_name, formula) VALUES
('Pfizer', 'Lipitor', 'C33H34FN2O5'),
('Pfizer', 'Viagra', 'C22H30N6O4S'),
('Pfizer', 'Xanax', 'C17H13ClN4'),
('Novartis', 'Diovan', 'C24H29N5O3'),
('Novartis', 'Gleevec', 'C29H31N7O'),
('Bayer', 'Aspirin', 'C9H8O4'),
('Bayer', 'Aleve', 'C14H14N2O3'),
('GlaxoSmithKline', 'Advair', 'C25H37FO5S'),
('GlaxoSmithKline', 'Ventolin', 'C13H21NO3'),
('Sun Pharma', 'Pantocid', 'C16H15F2N3O4S'),
('Johnson & Johnson', 'Tylenol', 'C8H9NO2'),
('Johnson & Johnson', 'Benadryl', 'C17H21NO'),
('Sanofi', 'Lantus', 'C267H404N72O78S6'),
('Sanofi', 'Ambien', 'C19H21N3O'),
('Roche', 'Valium', 'C16H13ClN2O'),
('Roche', 'Tamiflu', 'C16H28N2O4'),
('Merck', 'Januvia', 'C16H15F6N5O'),
('Merck', 'Zocor', 'C25H38O5'),
('AstraZeneca', 'Nexium', 'C17H19N3O3S'),
('AstraZeneca', 'Crestor', 'C22H28FN3O6S');

-- Pharmacy Data
INSERT INTO Pharmacy (ph_name, ph_add, ph_contact) VALUES
('MedPlus', '123 Main St, New York, NY', '+1-212-555-1234'),
('HealthMart', '456 Oak Ave, Chicago, IL', '+1-312-555-2345'),
('Wellness Pharmacy', '789 Pine Rd, San Francisco, CA', '+1-415-555-3456'),
('City Drugs', '101 Maple Blvd, Boston, MA', '+1-617-555-4567'),
('Care Pharmacy', '202 Elm St, Austin, TX', '+1-512-555-5678'),
('Quick Meds', '303 Cedar Ln, Seattle, WA', '+1-206-555-6789'),
('Family Pharma', '404 Birch Dr, Miami, FL', '+1-305-555-7890'),
('Apollo Pharmacy', '505 Willow Ave, Houston, TX', '+1-713-555-8901'),
('Lifecare Drugs', '606 Spruce St, Denver, CO', '+1-303-555-9012'),
('Metro Meds', '707 Aspen Ct, Atlanta, GA', '+1-404-555-0123');

-- Contract Data
INSERT INTO Contract (pc_name, start_date, end_date, content, supervisor, ph_name) VALUES
('Pfizer', '2023-01-01', '2025-12-31', 'Distribution agreement for all Pfizer products at standard discount rate', 'John Smith', 'MedPlus'),
('Novartis', '2023-02-15', '2025-02-14', 'Supply of cardiovascular and oncology products', 'Maria Garcia', 'MedPlus'),
('Bayer', '2023-03-10', '2025-09-09', 'Distribution of OTC products at 15% discount', 'Robert Johnson', 'HealthMart'),
('GlaxoSmithKline', '2023-04-01', '2025-03-31', 'Supply of respiratory medicines and vaccines', 'Sarah Williams', 'Wellness Pharmacy'),
('Sun Pharma', '2023-05-15', '2025-05-14', 'Generic drug distribution agreement', 'James Brown', 'City Drugs'),
('Johnson & Johnson', '2023-06-01', '2025-05-31', 'Consumer healthcare product supply', 'Emily Davis', 'Care Pharmacy'),
('Sanofi', '2023-07-15', '2025-07-14', 'Diabetes care product distribution', 'Michael Wilson', 'Quick Meds'),
('Roche', '2023-08-01', '2025-07-31', 'Oncology and immunology product supply', 'David Miller', 'Family Pharma'),
('Merck', '2023-09-15', '2025-09-14', 'Vaccines and biologics distribution', 'Laura Taylor', 'Apollo Pharmacy'),
('AstraZeneca', '2023-10-01', '2025-09-30', 'Respiratory and cardiovascular medicines supply', 'Daniel Anderson', 'Lifecare Drugs'),
('Pfizer', '2023-11-15', '2025-11-14', 'Premium partnership for all product lines', 'Jennifer Thomas', 'Metro Meds'),
('Bayer', '2023-12-01', '2025-11-30', 'Specialty drugs distribution agreement', 'Christopher White', 'MedPlus'),
('Novartis', '2024-01-10', '2026-01-09', 'Ophthalmology products supply', 'Lisa Martinez', 'Apollo Pharmacy'),
('GlaxoSmithKline', '2024-02-01', '2026-01-31', 'Vaccine distribution partnership', 'Kevin Robinson', 'Metro Meds'),
('Sun Pharma', '2024-03-15', '2026-03-14', 'General medicines supply agreement', 'Amanda Lee', 'HealthMart');

-- Pharmacy_Drugs Data
INSERT INTO Pharmacy_Drugs (pc_name, trade_name, price, ph_name,quantity) VALUES
('Pfizer', 'Lipitor', 120.50, 'MedPlus',300),
('Pfizer', 'Viagra', 95.75, 'MedPlus',250),
('Pfizer', 'Xanax', 45.25, 'MedPlus',100),
('Novartis', 'Diovan', 89.99, 'MedPlus',500),
('Bayer', 'Aspirin', 12.50, 'MedPlus',240),
('Pfizer', 'Lipitor', 125.99, 'HealthMart',320),
('Novartis', 'Gleevec', 325.50, 'HealthMart',270),
('Bayer', 'Aleve', 15.75, 'HealthMart',190),
('Sun Pharma', 'Pantocid', 32.99, 'HealthMart',340),
('GlaxoSmithKline', 'Advair', 210.25, 'Wellness Pharmacy',450),
('GlaxoSmithKline', 'Ventolin', 65.50, 'Wellness Pharmacy',290),
('Johnson & Johnson', 'Tylenol', 8.99, 'Wellness Pharmacy',380),
('Johnson & Johnson', 'Benadryl', 12.75, 'City Drugs',550),
('Sanofi', 'Lantus', 275.50, 'City Drugs',440),
('Sun Pharma', 'Pantocid', 30.25, 'City Drugs',390),
('Roche', 'Valium', 55.99, 'Care Pharmacy',550),
('Roche', 'Tamiflu', 95.25, 'Care Pharmacy',220),
('Merck', 'Januvia', 185.50, 'Quick Meds',660),
('Merck', 'Zocor', 110.75, 'Quick Meds',520),
('AstraZeneca', 'Nexium', 125.99, 'Family Pharma',410),
('AstraZeneca', 'Crestor', 155.50, 'Family Pharma',800),
('Pfizer', 'Xanax', 47.99, 'Apollo Pharmacy',380),
('Novartis', 'Diovan', 92.50, 'Apollo Pharmacy',70),
('Bayer', 'Aspirin', 13.25, 'Lifecare Drugs',340),
('Johnson & Johnson', 'Tylenol', 9.50, 'Lifecare Drugs',370),
('Sanofi', 'Ambien', 75.25, 'Metro Meds',90),
('AstraZeneca', 'Nexium', 129.99, 'Metro Meds',100);

-- Doctor Data
INSERT INTO Doctor (d_name, spec, years_of_exp, d_aadhar) VALUES
('Dr. John Carter', 'Cardiology', 15, '123456789012'),
('Dr. Meredith Grey', 'Neurology', 12, '234567890123'),
('Dr. Gregory House', 'Diagnostics', 20, '345678901234'),
('Dr. Cristina Yang', 'Cardiothoracic', 10, '456789012345'),
('Dr. Derek Shepherd', 'Neurosurgery', 18, '567890123456'),
('Dr. Lisa Cuddy', 'Administration', 22, '678901234567'),
('Dr. Miranda Bailey', 'General Surgery', 16, '789012345678'),
('Dr. James Wilson', 'Oncology', 19, '890123456789'),
('Dr. Allison Cameron', 'Immunology', 8, '901234567890'),
('Dr. Richard Webber', 'General Surgery', 30, '012345678901');

-- Patient Data
INSERT INTO Patient (p_name, p_add, p_age, p_aadhar, p_doc_aid) VALUES
('Robert Brown', '123 First St, New York, NY', 45, '111222333444', '123456789012'),
('Susan White', '456 Second Ave, Los Angeles, CA', 32, '222333444555', '234567890123'),
('Michael Johnson', '789 Third Blvd, Chicago, IL', 58, '333444555666', '345678901234'),
('Emily Davis', '101 Fourth Dr, Houston, TX', 29, '444555666777', '456789012345'),
('David Wilson', '202 Fifth Ln, Phoenix, AZ', 67, '555666777888', '567890123456'),
('Jennifer Smith', '303 Sixth St, Philadelphia, PA', 41, '666777888999', '678901234567'),
('James Miller', '404 Seventh Ave, San Antonio, TX', 36, '777888999000', '789012345678'),
('Lisa Garcia', '505 Eighth Rd, San Diego, CA', 52, '888999000111', '890123456789'),
('Thomas Rodriguez', '606 Ninth Blvd, Dallas, TX', 47, '999000111222', '901234567890'),
('Sarah Martinez', '707 Tenth Dr, San Jose, CA', 63, '000111222333', '012345678901'),
('Charles Taylor', '808 Eleventh St, Austin, TX', 39, '112233445566', '123456789012'),
('Mary Anderson', '909 Twelfth Ave, Jacksonville, FL', 55, '223344556677', '234567890123'),
('Daniel Thomas', '110 Thirteenth Ln, San Francisco, CA', 42, '334455667788', '345678901234'),
('Patricia Jackson', '211 Fourteenth Rd, Indianapolis, IN', 71, '445566778899', '456789012345'),
('Christopher Harris', '312 Fifteenth St, Columbus, OH', 33, '556677889900', '567890123456'),
('Nancy Clark', '413 Sixteenth Ave, Fort Worth, TX', 48, '667788990011', '678901234567'),
('Matthew Lewis', '514 Seventeenth Dr, Charlotte, NC', 59, '778899001122', '789012345678'),
('Elizabeth Lee', '615 Eighteenth Rd, Detroit, MI', 27, '889900112233', '890123456789'),
('Joseph Walker', '716 Nineteenth St, El Paso, TX', 64, '990011223344', '901234567890'),
('Margaret Hall', '817 Twentieth Ave, Seattle, WA', 51, '001122334455', '012345678901');

-- Prescription Data
INSERT INTO Prescription (pr_date, p_id, d_id) VALUES
('2024-01-05', '111222333444', '123456789012'),
('2024-01-07', '222333444555', '234567890123'),
('2024-01-10', '333444555666', '345678901234'),
('2024-01-12', '444555666777', '456789012345'),
('2024-01-15', '555666777888', '567890123456'),
('2024-01-20', '666777888999', '678901234567'),
('2024-01-22', '777888999000', '789012345678'),
('2024-01-25', '888999000111', '890123456789'),
('2024-01-27', '999000111222', '901234567890'),
('2024-02-01', '000111222333', '012345678901'),
('2024-02-03', '112233445566', '123456789012'),
('2024-02-05', '223344556677', '234567890123'),
('2024-02-08', '334455667788', '345678901234'),
('2024-02-10', '445566778899', '456789012345'),
('2024-02-12', '556677889900', '567890123456'),
('2024-02-15', '667788990011', '678901234567'),
('2024-02-18', '778899001122', '789012345678'),
('2024-02-20', '889900112233', '890123456789'),
('2024-02-22', '990011223344', '901234567890'),
('2024-02-25', '001122334455', '012345678901'),
('2024-03-01', '111222333444', '123456789012'),
('2024-03-05', '222333444555', '234567890123'),
('2024-03-08', '333444555666', '345678901234'),
('2024-03-10', '444555666777', '456789012345'),
('2024-03-12', '555666777888', '567890123456');

-- Prescription_Drugs Data
INSERT INTO Prescription_Drugs (pc_name, trade_name, pr_no, quantity) VALUES
('Johnson & Johnson', 'Tylenol', 1, 20),
('Pfizer', 'Lipitor', 1, 30),
('Pfizer', 'Viagra', 2, 10),
('Novartis', 'Gleevec', 3, 60),
('GlaxoSmithKline', 'Ventolin', 4, 1),
('Bayer', 'Aspirin', 5, 100),
('Johnson & Johnson', 'Tylenol', 6, 30),
('Sanofi', 'Lantus', 7, 5),
('Roche', 'Tamiflu', 8, 10),
('Merck', 'Januvia', 9, 30),
('AstraZeneca', 'Nexium', 10, 28),
('Pfizer', 'Xanax', 11, 20),
('Novartis', 'Diovan', 12, 30),
('Bayer', 'Aleve', 13, 40),
('GlaxoSmithKline', 'Advair', 14, 1),
('Sun Pharma', 'Pantocid', 15, 14),
('Johnson & Johnson', 'Benadryl', 16, 30),
('Sanofi', 'Ambien', 17, 14),
('Roche', 'Valium', 18, 20),
('Merck', 'Zocor', 19, 30),
('AstraZeneca', 'Crestor', 20, 30),
('Pfizer', 'Lipitor', 21, 30),
('Bayer', 'Aspirin', 22, 60),
('Johnson & Johnson', 'Tylenol', 23, 20),
('Sanofi', 'Lantus', 24, 3),
('Novartis', 'Gleevec', 25, 30);
