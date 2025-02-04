-- This file contains the demonstration queries to show that the database is working and fulfills the requirements of the client

-- Retrieve all flights that are departing from Birmingham
-- SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE origin = 'Birmingham';

-- Retrieve all flights that are going to Ibiza
-- SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE destination = 'Ibiza';

-- Retrieve all flights that are cancelled
-- SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE status = 'Cancelled';

-- Retrieve all flights that are after a certain date
-- SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE departuredate > '2025-02-03';

-- Retrieve all flights that are from Birmingham and delayed
-- SELECT flight_ID, origin,destination,departuretime,departuredate FROM flights WHERE origin = 'Birmingham' AND status ='Delayed';

-- Retrieve all flights that are from Birmingham and to Spain
-- SELECT * FROM (SELECT * FROM flights JOIN destinations ON flights.destination=destinations.name WHERE country = 'Spain') WHERE origin = 'Birmingham';

-- Change a flight status to delayed
-- UPDATE flights SET status = 'Delayed' WHERE flight_ID = 6;
--SELECT * FROM flights;

-- Change a departure time
-- UPDATE flights SET departuretime = '12:30:00' WHERE flight_ID = 7;
-- SELECT * FROM flights;

-- Change all flights from Birmingham to delayed
-- UPDATE flights SET status = 'Delayed' WHERE origin = 'Birmingham';
-- SELECT * FROM flights;

-- Change all flights to Spain to cancelled
--UPDATE (SELECT * FROM flights JOIN destinations ON flights.destination=destinations.name) SET status = 'Cancelled' WHERE country = 'Spain';

--UPDATE flights SET status = 'Cancelled' WHERE flight_ID in (SELECT flight_ID FROM flights JOIN destinations ON flights.destination=destinations.name WHERE country = 'Spain');
SELECT * FROM flights;