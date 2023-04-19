import sqlite3

conn = sqlite3.connect('db/wireWolf.db')
curr = conn.cursor()

curr.execute("""
SELECT * from ruangan;
""")

data = curr.fetchall()
print(data)
