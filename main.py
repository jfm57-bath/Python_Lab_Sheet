import sqlite3
conn = sqlite3.connect('store')
print ("Database has been created")

firstnames = ['Pedro', 'William', 'Numaan', 'Themiya', 'Mohammed', 'Thomas','Sarah', 'Zoe', 'Natalie','Alice','Verity','Zainab','Peter','James','Joanna','Sinead']
surnames = ['Jones','Mason','Murphy','Sanchez','Disraeli','Higgins','Smith','Gladstone','Cameron','Rubio','Fitzgerald','Western','Brown','McGlynn','McGrath','Siriwardhana']
pilotID = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']


cities = ['Birmingham','Manchester','London','Bristol','Paris','Toulouse','Berlin','Madrid','Barcelona','Ibiza','Rome','Florence','Geneva','Frankfurt']

# def time():
#     conn.execute(SELECT datetime(strftime('%s', '2000-01-01 00:00:00') + abs(random() % (strftime('%s', '2000-01-31 23:59:59') - strftime('%s', '2000-01-01 00:00:00') )),'unixepoch');

def create_flights():
    conn.execute("DROP TABLE IF EXISTS flights")
    conn.execute("CREATE TABLE flights (flight_ID VARCHAR(20), origin VARCHAR(20), destination VARCHAR(20), pilotID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20))")
    # time = time()
    conn.execute("INSERT INTO flights (flight_ID,origin,destination,pilotID,departuredate,departuretime)VALUES \
  ('LS1339','Birmingham','Vienna','1','2025-02-04','" + "12:00:00" + "')")

def create_destinations():
    conn.execute("DROP TABLE IF EXISTS destinations")
    conn.execute("CREATE TABLE destinations (destination_ID VARCHAR(20), latitude VARCHAR(20), longitude VARCHAR(20))")

def create_pilots():
    conn.execute("DROP TABLE IF EXISTS pilots")
    conn.execute("CREATE TABLE pilots (pilot_ID VARCHAR(20), forename VARCHAR(20), surname VARCHAR(20))")
    i = 0
    for name in firstnames:
        conn.execute("INSERT INTO pilots (pilot_ID,forename,surname)VALUES \
  ('" + pilotID[i] +"','" + name + "','" + str(surnames[i]) + "')")
        i = i+1

def check_item(table, column, name):
    # check whether an item is an a column of a specific table.
    test = conn.execute("SELECT COUNT(1) FROM " + table + " WHERE "+ column + " = '" +  name + "';") #this works
    if next(test)[0] == 1:
        return True
    else:
        return False   

def add_flight(parameters):
    print("Please type the origin of the flight")
    temp_origin = input()
    if check_item('flight', 'destination', temp_origin) == False:
        print("Origin not found, please select an origin")
    else:
        origin = temp_origin
    print("Please type the destination of the flight")
    temp_destination = input()
    print(str(parameters) + 'parameters')
    conn.execute("INSERT INTO flights (flight_ID,origin,destination,pilotID,departuredate,departuretime)VALUES \
  ('BHX455','Birmingham','Ibiza','123','2001-02-04','15:23')")
    conn.commit()

def view_schedule(name,surname):
    print("Please type the forename of the pilot")
    print("Please type the surname of the pilot")
    # check that the pilot is included in the list
    if check_item('flight', 'destination', temp_origin) == False:
        print("Origin not found, please select an origin")
    # if name == '' and surname == '':
    #     print('Showing list of pilots')
    #     #show list of pilots and prompt to select from list.
    # else:
    #     print('Searching records')
    print("Query")
    cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights")
    for row in cursor:
        print("origin = ", row[0])
        print("destination = ", row[1])
        print("date = ", row[2])
        print("time = ", row[3], "\n")

def assign(pilot_ID,flight_ID):
    #change line below to a query for flights that currently don't have a pilot assigned. 
    cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights")
    for row in cursor:
        print("origin = ", row[0])
        print("destination = ", row[1])
        print("date = ", row[2])
        print("time = ", row[3], "\n")
    ##Allow the user to select one of flights by ID
    ##Show list of pilots
    ##Add an update to change the field. 
    print('Assigning pilot to this flight')
    conn.commit()

def view_flights():
    cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights")
    for row in cursor:
        print("origin = ", row[0])
        print("destination = ", row[1])
        print("date = ", row[2])
        print("time = ", row[3], "\n")
    print('viewing flights')

def view_pilots():
    cursor = conn.execute("SELECT pilot_ID,forename,surname from pilots")
    for row in cursor:
        print("pilot_ID = ", row[0])
        print("forename = ", row[1])
        print("surname = ", row[2], "\n")
    print('viewing pilots')

def update_flight():
    print('updating flights')
    print("What is the flightID that you want to edit?")
    ##check whether the flight is included in the list

def welcome_sequence():
    print("Welcome to the flight management system. You can use the command line to enter your commands.")
    print("The avaiable commands are, ADD, VIEW, etc.")

#######

#have two different commands. One for the actual sql action. The other for the sequence with inputs etc.
#call the UI input first. 
#######

def commands(letter):
    #All commands have two options for usage. Either state the command and then it will walk you through the options. Or if you know the innputs already you can enter them.
    match letter[0]:
        case 'ADD':
            return (add_flight('test'))
        case 'VIEWFLIGHTS': #view all the flights in the database
            return (view_flights())
        case 'UPDATE':
            return (update_flight())
        case 'VIEWPILOTS':
            return(view_pilots())
        case 'ASSIGN':
            return (assign())
        case 'VIEWSCHEDULE':
            return (view_schedule())
        case 'VIEWDESTINTATIONS':
            return (view_destinations())
        case 'UPDATEDESTINATION':
            return (update_destination)
        case 'ADDDESTINATION':
            return (add_destination())

def process_command(string):
    result = string.split()
    print(result)
    print(commands(result))


def initialise():
    create_flights()
    welcome_sequence()
    create_destinations()
    create_pilots()

###################
main_loop = True

check_item('flights','destination','Vienna')

def main_loop_fct():
    while main_loop == True:
        process_command(input())

if __name__== '__main__':
    initialise()
    main_loop_fct()
