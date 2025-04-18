CREATE database pharmadb;
USE pharmadb;

CREATE TABLE PharmaCompany(
	pc_name varchar(255) NOT NULL,
    pc_contact bigint,
    
    primary key(pc_name)
);

CREATE TABLE Drugs(
	pc_name varchar(255) NOT NULL,
    trade_name varchar(255) NOT NULL,
    formula varchar(255),
    
    primary key(trade_name),
    foreign key(pc_name) references PharmaCompany(pc_name)
);

CREATE TABLE Pharmacy(
	ph_name varchar(255) NOT NULL,
    ph_add varchar(255),
    ph_contact bigint,
    
    primary key(ph_name)
);

CREATE TABLE Contract(
	pc_name varchar(255) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
	content varchar(255) NOT NULL,
    supervisor varchar(255),
    ph_name varchar(255) NOT NULL,
    
    foreign key(pc_name) references PharmaCompany(pc_name),
    foreign key(ph_name) references Pharmacy(ph_name)
);

CREATE TABLE Pharmacy_Drugs(
	pc_name varchar(255) NOT NULL,
    trade_name varchar(255) NOT NULL,
    price int,
    ph_name varchar(255) NOT NULL,
    
    foreign key(ph_name) references Pharmacy(ph_name),
    foreign key(pc_name) references PharmaCompany(pc_name),
    foreign key(trade_name) references Drugs(trade_name)
);

CREATE TABLE Doctor(
	d_name varchar(255),
    spec varchar(255),
    years_of_exp int,
    d_aadhar bigint NOT NULL,
    
    primary key(d_aadhar)
);

CREATE TABLE Patient(
	p_name varchar(255) ,
    p_add varchar(255) ,
    p_age int,
    p_aadhar bigint NOT NULL,
    p_doc_aid bigint NOT NULL,
    
    primary key(p_aadhar),
    foreign key(p_doc_aid) references Doctor(d_aadhar)
);

CREATE TABLE Prescription(
	pr_no int NOT NULL,
    pr_date date NOT NULL,
    p_id bigint NOT NULL,
    d_id bigint NOT NULL,
    
    UNIQUE(p_id,d_id,pr_date),
    primary key(pr_no),
    foreign key(p_id) references Patient(p_aadhar),
    foreign key(d_id) references Doctor(d_aadhar)
);

CREATE TABLE Prescription_Drugs(
	pc_name varchar(255) NOT NULL,
    trade_name varchar(255) NOT NULL,
    pr_no int NOT NULL,
    quantity int NOT NULL,
    
    foreign key(pc_name) references PharmaCompany(pc_name),
    foreign key(pr_no) references Prescription(pr_no),
    foreign key(trade_name) references Drugs(trade_name)
    
);
