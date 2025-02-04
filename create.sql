-- This SQL file contains the scripts to create the tables within the database and prepopulate with data

DROP TABLE IF EXISTS flights;

CREATE TABLE flights (flight_ID VARCHAR(20), origin VARCHAR(20), destination VARCHAR(20), pilotID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20), PRIMARY KEY (flight_ID));

