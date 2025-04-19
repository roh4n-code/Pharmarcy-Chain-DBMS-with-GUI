CREATE DATABASE pharmadb;
USE pharmadb;

CREATE TABLE PharmaCompany(
	pc_name VARCHAR(50) NOT NULL,
    pc_contact VARCHAR(30),
    
    PRIMARY KEY(pc_name)
);

CREATE TABLE Drugs(
	pc_name VARCHAR(50) NOT NULL,
    trade_name VARCHAR(50) NOT NULL,
    formula VARCHAR(255),
    
    PRIMARY KEY(trade_name),
    FOREIGN KEY(pc_name) references PharmaCompany(pc_name)
);

CREATE TABLE Pharmacy(
	ph_name VARCHAR(50) NOT NULL,
    ph_add VARCHAR(255),
    ph_contact VARCHAR(30),
    
    PRIMARY KEY(ph_name)
);

CREATE TABLE Contract(
	pc_name VARCHAR(50) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
	content VARCHAR(500) NOT NULL,
    supervisor VARCHAR(50),
    ph_name VARCHAR(50) NOT NULL,
    
    PRIMARY KEY(pc_name,ph_name),
    FOREIGN KEY(pc_name) references PharmaCompany(pc_name),
    FOREIGN KEY(ph_name) references Pharmacy(ph_name),
    
    CHECK(end_date > start_date)
);

CREATE TABLE Pharmacy_Drugs(
	pc_name VARCHAR(50) NOT NULL,
    trade_name VARCHAR(50) NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    ph_name VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    
    PRIMARY KEY (pc_name,trade_name,ph_name),
    FOREIGN KEY(ph_name) references Pharmacy(ph_name),
    FOREIGN KEY(pc_name) references PharmaCompany(pc_name),
    FOREIGN KEY(trade_name) references Drugs(trade_name),
    
    CHECK(price > 0 AND quantity > 0)
);

CREATE TABLE Doctor(
	d_name VARCHAR(50),
    spec VARCHAR(30),
    years_of_exp INT,
    d_aadhar VARCHAR(12) NOT NULL,
    
    PRIMARY KEY(d_aadhar),
    
    CHECK (years_of_exp > 0)
);

CREATE TABLE Patient(
	p_name VARCHAR(50) NOT NULL,
    p_add VARCHAR(255) ,
    p_age INT NOT NULL,
    p_aadhar VARCHAR(12) NOT NULL,
    p_doc_aid VARCHAR(12) NOT NULL,
    
    PRIMARY KEY(p_aadhar),
    FOREIGN KEY(p_doc_aid) references Doctor(d_aadhar),
    
    CHECK (p_age >= 0) 
);

CREATE TABLE Prescription(
	pr_no INT auto_increment,
    pr_date date NOT NULL,
    p_id VARCHAR(12) NOT NULL,
    d_id VARCHAR(12) NOT NULL,
    
    UNIQUE(p_id,d_id,pr_date),
    PRIMARY KEY(pr_no),
    FOREIGN KEY(p_id) references Patient(p_aadhar),
    FOREIGN KEY(d_id) references Doctor(d_aadhar)
);

CREATE TABLE Prescription_Drugs(
	pc_name VARCHAR(50) NOT NULL,
    trade_name VARCHAR(50) NOT NULL,
    pr_no INT NOT NULL,
    quantity INT NOT NULL,
    
    PRIMARY KEY(pc_name,trade_name,pr_no),    
    FOREIGN KEY(pc_name) references PharmaCompany(pc_name),
    FOREIGN KEY(pr_no) references Prescription(pr_no),
    FOREIGN KEY(trade_name) references Drugs(trade_name)
);