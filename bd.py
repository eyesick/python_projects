import sqlite3
people = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
)

connection = sqlite3.connect(':memory:')
with connection:
    c = connection.cursor()
    c.execute("""DROP TABLE IF EXISTS People""")
    c.execute("""CREATE TABLE People(FirstName Text, species TEXT, iq INT)""")
    c.executemany('INSERT INTO People (FirstName, species, iq) VALUES (?, ?, ?)', people)
    c.execute("""UPDATE People SET species = 'Human' WHERE species = 'Meat Popsicle'""")
    c.execute("""SELECT * from People WHERE species = 'Human'""")
    result = c.fetchall()
    print(result)
