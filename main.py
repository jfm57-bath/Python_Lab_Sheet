import sqlite3
conn = sqlite3.connect('store')
print ("Database has been created")


def create_flights():
    conn.execute("DROP TABLE IF EXISTS flights")
    conn.execute("CREATE TABLE flights (flight_ID VARCHAR(20), origin VARCHAR(20), destination VARCHAR(20), pilotID VARCHAR(20), departuredate DATE, departuretime VARCHAR(20))")

def create_destinations():
    conn.execute("DROP TABLE IF EXISTS destinations")
    conn.execute("CREATE TABLE destinations (destination_ID VARCHAR(20), latitude VARCHAR(20), longitude VARCHAR(20))")

def create_pilots():
    conn.execute("DROP TABLE IF EXISTS pilots")
    conn.execute("CREATE TABLE pilots (pilot_ID VARCHAR(20), forename VARCHAR(20), surname VARCHAR(20))")

def add_flight(parameters):
    print(str(parameters) + 'parameters')
    conn.execute("INSERT INTO flights (flight_ID,origin,destination,pilotID,departuredate,departuretime)VALUES \
  ('BHX455','Birmingham','Ibiza','123','2001-02-04','')")
    conn.commit()

def view_schedule(name,surname):
    if name == '' and surname == '':
        print('Showing list of pilots')
        #show list of pilots and prompt to select from list.
    else:
        print('Searching records')

def assign(pilot_ID,flight_ID):
    print('Assigning')

def view_flights():
    print('viewing flights')

def update_flight():
    print('updating flights')


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
create_destinations()
create_pilots()




while main == True:
    process_command(input())
    



