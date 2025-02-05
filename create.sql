-- This SQL file contains the scripts to create the tables within the database and prepopulate with data

-- Create table
DROP TABLE IF EXISTS flights;
CREATE TABLE flights (flight_ID INTEGER PRIMARY KEY NOT NULL, origin VARCHAR(20), status VARCHAR(20), destination VARCHAR(20), pilot_ID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20),plane_ID INTEGER);
INSERT INTO flights (origin,destination,pilot_ID,departuredate,departuretime,status)VALUES
   ('Birmingham','Vienna','1','2025-02-03','12:00:00','On time'),
   ('Birmingham','London','2','2025-02-03','17:00:00','On time'),
   ('Birmingham','Madrid','3','2025-02-03','14:00:00','On time'),
   ('Birmingham','Prague','4','2025-02-03','09:00:00','On time'),
   ('London','Vienna','5','2025-02-03','08:00:00','On time'),
   ('Birmingham','Ibiza','6','2025-02-03','12:30:00','On time'),
   ('Vienna','London','7','2025-02-04','11:40:00','On time'),
   ('Manchester','Ibiza','8','2025-02-04','15:10:00','On time'),
   ('London','Ibiza','9','2025-02-04','13:15:00','Cancelled'),
   ('London','Vienna','10','2025-02-04','19:20:00','On time'),
   ('Vienna','London','11','2025-02-04','21:30:00','Delayed'),
   ('Birmingham','Vienna','1','2025-02-05','22:00:00','On time'),
   ('London','Frankfurt','2','2025-02-05','04:30:00','Cancelled'),
   ('Manchester','Frankfurt','3','2025-02-05','08:50:00','Delayed'),
   ('Birmingham','Berlin','4','2025-02-05','13:10:00','Cancelled');

-- Create flights without pilot assigned
INSERT INTO flights (origin,destination,departuredate,departuretime)VALUES
   ('Birmingham','Ibiza','2025-02-06','12:30:00'),
   ('Berlin','Vienna','2025-02-06','11:30:00'),
   ('Ibiza','London','2025-02-06','16:30:00'),
   ('Barcelona','London','2025-02-07','18:50:00'),
   ('Madrid','Birmingham','2025-02-07','20:10:00');

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

-- Create table for pilots
DROP TABLE IF EXISTS pilots;
CREATE TABLE pilots (pilot_ID INTEGER PRIMARY KEY NOT NULL, forename VARCHAR(20), surname VARCHAR(20), sex VARCHAR(1), DOB DATE);
INSERT INTO pilots (forename,surname,sex,DOB)VALUES
   ('William','Jones','m','1978-01-12'),
   ('Pedro','Sanchez','m','1988-02-15'),
   ('William','Disraeli','m','1979-07-23'),
   ('Numaan','Higgins','m','1991-03-11'),
   ('Themiya','Cameron','m','1995-11-11'),
   ('Zoe','Mason','f','1989-10-10'),
   ('Sarah','Long','f','1969-01-01'),
   ('Hillary','Clinton','f','1983-12-12'),
   ('Charlotte','West','f','1986-09-27'),
   ('Prita','Ali','f','1994-01-01'),
   ('Zainab','Amar','f','1991-08-03');

-- Create table for planes
 DROP TABLE IF EXISTS planes;
 CREATE TABLE planes (plane_ID INTEGER PRIMARY KEY NOT NULL, model VARCHAR(20), commissiondate VARCHAR(20));
 INSERT INTO planes (model,commissiondate)VALUES
   ('Boeing','2005-01-01'),
   ('Airbus','2009-01-01'),
   ('Lockhead Martin','2016-01-01'),
   ('Boeing','2014-01-01');

