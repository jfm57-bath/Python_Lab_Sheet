import sqlite3
conn = sqlite3.connect('store')
print ("Database has been created")

def create_flights():
    conn.execute("DROP TABLE IF EXISTS flights")
    conn.execute("CREATE TABLE flights (flight_ID VARCHAR(20), origin VARCHAR(20), destination VARCHAR(20), pilotID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20))")

def check_item(table, column, name):
    # check whether an item is an a column of a specific table.
    # conn.execute
    print("Testing whether it is in")

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
    if name == '' and surname == '':
        print('Showing list of pilots')
        #show list of pilots and prompt to select from list.
    else:
        print('Searching records')
    print("Query")
    cursor = conn.execute("SELECT origin,destination,departuredate,departuretime from flights")
    for row in cursor:
        print("origin = ", row[0])
        print("destination = ", row[1])
        print("date = ", row[2])
        print("time = ", row[3], "\n")

def assign(pilot_ID,flight_ID):
    print('Assigning')

def view_flights():
    print('viewing flights')

def update_flight():
    print('updating flights')


def welcome_sequence():
    print("Welcome to the flight management system. You can use the command line to enter your commands.")
    print("The avaiable commands are, ADD, VIEW, etc.")


def commands(letter):
    #All commands have two options for usage. Either state the command and then it will walk you through the options. Or if you know the innputs already you can enter them.
    print(letter[0])
    match letter[0]:
        case 'ADD':
            return (add_flight(letter[1]))
        case 'VIEWFLIGHTS':
            return (view_flights(letter[1],letter[2]))
        case 'UPDATE':
            return (update_flight(letter[1]))
        case 'ASSIGN':
            return (assign(letter[1],letter[2]))
        case 'VIEWSCHEDULE':
            return (view_schedule(letter[1],letter[2]))
        case 'VIEWDESTINTATION':
            return print('hello')
        case 'UPDATEDESTINATION':
            return print('test')
        case 'ADDDESTINATION':
            return print('test')

def process_command(string):
    result = string.split()
    print(result)
    print(commands(result))

main = True

create_flights()
welcome_sequence()



while main == True:
    process_command(input())
    



