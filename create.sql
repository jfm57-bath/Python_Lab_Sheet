-- This SQL file contains the scripts to create the tables within the database and prepopulate with data

DROP TABLE IF EXISTS flights
CREATE TABLE Persons
    (PersonID INTEGER NOT NULL AUTO_INCREMENT,
     Name VARCHAR(40),
     DoB DATE,
     PRIMARY KEY (PersonID));