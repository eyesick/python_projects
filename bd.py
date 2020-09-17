import sqlite3

connection = sqlite3.connect(':memory:')
c = connection.cursor()
c.execute("""DROP TABLE IF EXISTS People""")
c.execute("""CREATE TABLE People(FirstName Text, species TEXT, iq INT)""")
        
			
