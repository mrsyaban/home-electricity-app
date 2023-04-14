import sqlite3

conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()
print(rows)

class   