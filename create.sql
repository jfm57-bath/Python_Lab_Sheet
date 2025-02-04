-- This SQL file contains the scripts to create the tables within the database and prepopulate with data

-- Create table
DROP TABLE IF EXISTS flights;
CREATE TABLE flights (flight_ID VARCHAR(20), origin VARCHAR(20), status VARCHAR(20), destination VARCHAR(20), pilot_ID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20), PRIMARY KEY (flight_ID));
INSERT INTO flights (flight_ID,origin,destination,pilot_ID,departuredate,departuretime)VALUES
   ('1','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('2','Birmingham','London','1','2025-02-04','12:00:00'),
   ('3','Birmingham','Madrid','1','2025-02-04','12:00:00'),
   ('4','Birmingham','Prague','1','2025-02-04','12:00:00'),
   ('5','London','Vienna','1','2025-02-04','12:00:00'),
   ('6','Birmingham','Ibiza','1','2025-02-04','12:00:00'),
   ('7','Vienna','London','1','2025-02-04','12:00:00'),
   ('8','Manchester','Ibiza','1','2025-02-04','12:00:00'),
   ('9','Manchester','Ibiza','1','2025-02-04','12:00:00'),
   ('10','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('11','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('12','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('13','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('14','Birmingham','Vienna','1','2025-02-04','12:00:00'),
   ('15','Birmingham','Vienna','1','2025-02-04','12:00:00');

-- Create table
DROP TABLE IF EXISTS destinations;
CREATE TABLE destinations (destination_ID VARCHAR(3), name VARCHAR(20), latitude VARCHAR(20), longitude VARCHAR(20), country VARCHAR(20));
INSERT INTO destinations (destination_ID,name,latitude,longitude,country)VALUES
   ('BHX','Birmingham','1','1','England'),
   ('VIE','Vienna','1','1','Austria'),
   ('LCY','London','1','1','England'),
   ('MAN','Manchester','1','1','England'),
   ('IBZ','Ibiza','1','1','Spain'),
   ('MAD','Madrid','1','1','Spain'),
   ('BER','Berlin','1','1','Germany'),
   ('VLC','Valencia','1','1','Spain'),
   ('FRA','Frankfurt','1','1','Germany'),
   ('BCN','Barcelona','1','1','Spain'),
   ('DEL','Delhi','1','1','India');

-- Create table
DROP TABLE IF EXISTS pilots;
CREATE TABLE pilots (pilot_ID INTEGER PRIMARY KEY NOT NULL, forename VARCHAR(20), surname VARCHAR(20));
INSERT INTO pilots (forename,surname)VALUES
   ('William','Jones'),
   ('Pedro','Sanchez'),
   ('William','Disraeli'),
   ('Numaan','Higgins'),
   ('Themiya','Cameron'),
   ('Mohammed','Mason'),
   ('William','Jones'),
   ('William','Jones'),
   ('William','Jones'),
   ('William','Jones'),
   ('William','Jones');




