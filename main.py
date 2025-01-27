import sqlite3
conn = sqlite3.connect('store')
print ("Database has been created")

conn.execute("DROP TABLE IF EXISTS pet")

conn.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")

print ("Table created successfully")

conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
  ('Fluffy','Harold','cat','f',5,'2001-02-04','')")

conn.execute("INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES \
  ('Claws','Gwen','cat','m',2,'2000-03-17','')")

conn.commit()
print("Records created successfully")
print("Total number of rows created :", conn.total_changes)