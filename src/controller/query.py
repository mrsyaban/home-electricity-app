import sqlite3

conn = sqlite3.connect('wirewolf.db')
cursor = conn.cursor()

class Query :
    def insertHouse(newHouse) :
        

cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
print(rows)
