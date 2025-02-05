import sqlite3

def help():
    #Function to show help commands
    print("The commands are:")
    print("case 'ADD': #Add a New Flight")
    print("case 'FILTERFLIGHTS': #View Flights by Criteria")
    print("case 'UPDATESTATUS': #Update Flight Information")
    print("case 'ASSIGN': #Assign Pilot to Flight")
    print("case 'VIEWSCHEDULE': #View Pilot Schedule")
    print("case 'UPDATEDESTINATION': #View/Update Destination Information")
    print("case 'VIEWPILOTS': #View all pilot information")
    print("case 'VIEWFLIGHTS': #View all the flights in the database")

def create_tables():
    #Function to create the tables by executing the create.sql file
    try:
        with open('create.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
    except Exception as e:
    # Roll back changes if anything goes wrong and raise exception
        conn.rollback()
        raise e

def check_item(table, column, name):
    # Function to check whether an item is an a column of a specific table
    test = conn.execute("SELECT COUNT(1) FROM " + table + " WHERE "+ column + " = '" +  name + "';") #query to identify item from table
    if next(test)[0] == 1: #if found return true
        return True
    else: #if not found return false
        return False   

def add_flight(parameters):
    #Function to add a flight
    progress = False #boolean variable to control progression through steps
    while progress == False:
        print("Please type the origin of the flight")
        temp_origin = input()
        if check_item('destinations', 'name', temp_origin) == False:
            print("Origin not found, please select an origin")
        elif temp_origin == 'CANCEL':
            return None
        else:
            origin = temp_origin
            progress = True

    progress = False
    while progress == False:
        print("Please type the destination of the flight")
        temp_destination = input()
        if check_item('destinations', 'name', temp_origin) == False:
            print("Origin not found, please select an origin")
        elif temp_destination == 'CANCEL':
            return None
        else:
            progress = True

    print("Please enter the departure date")
    temp_departuredate = input()

    print("Please enter the departure time")
    temp_departuretime = input()

    try:
        conn.execute("INSERT INTO flights (origin,destination,departuredate,departuretime)VALUES \
        '"+ temp_origin + "','" + temp_destination + "','" + temp_departuredate +"','" + temp_departuretime + "')")
        conn.commit()
        print("Flight successfully added!")
    except Exception as e:
    # Roll back changes if anything goes wrong and raise exception
        conn.rollback()
        raise e

def view_schedule():
    print("Please type the forename of the pilot")
    temp_forename = input()
    print("Please type the surname of the pilot")
    temp_surname = input()

    #Check whether the combination of forename and surname can be found in the pilots table.

    try:
        cursor = conn.execute("SELECT pilot_ID from pilots WHERE forename = '" + temp_forename + "' AND surname = '" + temp_surname + "';")
        for row in cursor:
            print("pilot_ID = ", row[0])
            temp_pilot_ID = row[0]

        print("Query")
        cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights WHERE pilot_ID= '" + str(temp_pilot_ID) + "';")
    
        print("The flights for " + temp_forename + " " + temp_surname + " are:")
        for row in cursor:
            print("origin = ", row[0])
            print("destination = ", row[1])
            print("date = ", row[2])
            print("time = ", row[3], "\n")
    except Exception as e:
    # Roll back changes if anything goes wrong and raise exception
        conn.rollback()
        raise e

def assign():
    print("The flights that currently do not have a pilot are:") 
    cursor = conn.execute("SELECT flight_ID,origin,destination,departuredate,departuretime from flights WHERE pilot_ID IS NULL")
    
    for row in cursor:
        print("flight_ID = ", row[0])
        print("origin = ", row[1])
        print("destination = ", row[2])
        print("date = ", row[3])
        print("time = ", row[4], "\n")

    print("What is the flight_ID that you want to assign a pilot to?")
    temp_flight_ID = input()
    
    print("The pilots are:")
    cursor = conn.execute("SELECT pilot_ID,forename,surname from pilots")
    
    for row in cursor:
        print("pilot_ID = ", row[0])
        print("forename = ", row[1])
        print("surname = ", row[2],"\n")

    print("What is the pilot_ID that you want to assign to the flight?")
    temp_pilot_ID = input()

    try:
        conn.execute("UPDATE flights SET pilot_ID = '" + str(temp_pilot_ID) + "' WHERE flight_ID = '" + str(temp_flight_ID) + "';")
        conn.commit()
        print('Successfully assigned pilot to this flight')
    except Exception as e:
    # Roll back changes if anything goes wrong and raise exception
        conn.rollback()
        raise e  

def view_flights():
    #Command triggered by 'VIEWFLIGHTS'
    cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights")
    for row in cursor:
        print("origin = ", row[0])
        print("destination = ", row[1])
        print("date = ", row[2])
        print("time = ", row[3], "\n")
    print('viewing flights')

def filter_flight():
    print("What column do you want to filter by?")
    filter_column = input()
    print("What should this value equal?")
    filter_value = input()
    print("Filtering flights by criteria")
    cursor = conn.execute("SELECT flight_ID, origin,destination,departuredate,departuretime from flights WHERE " + filter_column + "= '" + filter_value + "';")
    for row in cursor:
        print("flight_ID = ", row[0])
        print("origin = ", row[1])
        print("destination = ", row[2])
        print("date = ", row[3])
        print("time = ", row[4], "\n")

def view_pilots():
    cursor = conn.execute("SELECT pilot_ID,forename,surname from pilots")
    for row in cursor:
        print("pilot_ID = ", row[0])
        print("forename = ", row[1])
        print("surname = ", row[2], "\n")
    print('viewing pilots')

def update_destination():
    print("updating destination")

def update_flight():
    #Command to update flight status
    print("What is the flightID that you want to edit?")
    temp_flight_ID = input()
    ##check whether the flight is included in the list
    if check_item('flights','flight_ID',temp_flight_ID) == False:
        print("There is no flight with this ID")
    else:
        cursor = conn.execute("SELECT status FROM flights WHERE flight_ID='" + temp_flight_ID + "';")
        for row in cursor:
            print("Current flight status = ", row[0])
        print("What is the new status of the flight")
        temp_status = input()
        cursor = conn.execute("UPDATE flights SET status = '" + temp_status + "' WHERE flight_ID = " + temp_flight_ID + ";")

def welcome_sequence():
    print("Welcome to the flight management system. The database has been created already.\nYou can use the command line to enter your commands to create, retrieve, update and delete data.")
    help()

def commands(letter):
    #All commands have two options for usage. Either state the command and then it will walk you through the options. Or if you know the innputs already you can enter them.
    match letter[0]:
        case 'ADD': #Add a New Flight
            return (add_flight('test'))
        case 'FILTERFLIGHTS': #View Flights by Criteria
            return(filter_flight())
        case 'UPDATESTATUS': #Update Flight Information
            return (update_flight()) 
        case 'ASSIGN': #Assign Pilot to Flight
            return (assign())
        case 'VIEWSCHEDULE': #View Pilot Schedule
            return (view_schedule())
        case 'UPDATEDESTINATION': #View/Update Destination Information
            return (update_destination())
        case 'VIEWPILOTS': #View all pilot information
            return(view_pilots())
        case 'VIEWFLIGHTS': #View all the flights in the database
            return (view_flights())
        case 'HELP':
            return help()
        case _:
            print("Command not found")
            return help()


def process_command(string):
    commands(string.split())
    # print(result)
    # print(commands(result))

def initialise():
    create_tables()
    welcome_sequence()

###################
main_loop = True
def main_loop_fct():
    #Main loop function that reads commands
    while main_loop == True:
        print("Please enter the command you wish to use:")
        process_command(input())

if __name__== '__main__':
    conn = sqlite3.connect('store.db')
    print ("Database has been created")
    initialise()
    main_loop_fct()
