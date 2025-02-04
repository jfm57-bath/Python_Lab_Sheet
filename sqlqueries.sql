-- This file contains the demonstration queries to show that the database is working and fulfills the requirements of the client

-- Retrieve all flights that are departing from Birmingham
SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE origin = 'Birmingham';

-- Retrieve all flights that are going to Ibiza
SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE destination = 'Ibiza';

-- Retrieve all flights that are cancelled
SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE status = 'Cancelled';

-- Retrieve all flights that are after a certain date
SELECT flight_ID,origin,destination,departuretime,departuredate FROM flights WHERE departuredate > '2025-02-03';

