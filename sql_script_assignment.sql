CREATE DATABASE registration_db;

-- Create Table command  
CREATE TABLE Registration (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Address VARCHAR(255),
    Gender ENUM('Male', 'Female', 'Other')
);


 -- To read all records 
select * from registration;


--  update table add constraint 
ALTER TABLE Registration
ADD CONSTRAINT unique_email UNIQUE (Email);

-- adding data 
INSERT INTO Registration (FirstName, LastName, Email, DateOfBirth, Address, Gender)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '1990-05-15', '123 Main St, Anytown, USA', 'Male'),
    ('Jane', 'Smith', 'jane.smith@example.com', '1995-08-20', '456 Elm St, Othertown, USA', 'Female'),
    ('Alex', 'Johnson', 'alex.johnson@example.com', '1988-12-10', '789 Oak St, Somewhere, USA', 'Other');
    
    
INSERT INTO Registration (FirstName, LastName, Email, DateOfBirth, Address, Gender)
VALUES ('Raju', 'Singh', 'raju.singh@example.com', '1993-02-25', '145 Main St, Anytown, INDIA', 'Male');

INSERT INTO Registration (FirstName, LastName, Email, DateOfBirth, Address, Gender)
VALUES ('Raju', 'Singh2', 'raju2.singh@example.com', '1993-02-15', '1425 Main St, Anytown, INDIA', 'Male');


-- delete records 
DELETE FROM Registration
WHERE ID BETWEEN 4 AND 11;

