import sqlite3

def create_tables():
    with open('create.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()

def check_item(table, column, name):
    # check whether an item is an a column of a specific table.
    test = conn.execute("SELECT COUNT(1) FROM " + table + " WHERE "+ column + " = '" +  name + "';") #this works
    if next(test)[0] == 1:
        return True
    else:
        return False   

def add_flight(parameters):
    progress = False
    while progress == False:
        print("Please type the origin of the flight")
        temp_origin = input()
        if check_item('destinations', 'name', temp_origin) == False:
            print("Origin not found, please select an origin")
        else:
            origin = temp_origin
            progress = True

    progress = False
    while progress == False:
        print("Please type the destination of the flight")
        temp_destination = input()
        if check_item('destinations', 'name', temp_origin) == False:
            print("Origin not found, please select an origin")
        else:
            destination = temp_destination ##do a lookup here
            progress = True

    print("Please enter the departure date")
    temp_departuredate = input()
    print("Please enter the departure time")
    temp_departuretime = input()

    conn.execute("INSERT INTO flights (flight_ID, origin,destination,pilot_ID,departuredate,departuretime)VALUES \
  ('BHX455','Birmingham','" + temp_destination + "','123','" + temp_departuredate +"','" + temp_departuretime + "')")
    conn.commit()

    print("Flight successfully added!")

def view_schedule(name,surname):
    print("Please type the forename of the pilot")
    print("Please type the surname of the pilot")
    # check that the pilot is included in the list
    # if check_item('flight', 'destination', temp_origin) == False:
    #     print("Origin not found, please select an origin")
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
    #Command triggered by 'VIEWFLIGHTS'
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
        case 'ADD': #add a flight 
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
        # case 'VIEWDESTINTATIONS':
        #     return (view_destinations())
        # case 'UPDATEDESTINATION':
        #     return (update_destination)
        # case 'ADDDESTINATION':
        #     return (add_destination())

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
