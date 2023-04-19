import sqlite3

class HouseManager :
    def __init__(self) :
        self.id = ""

    def getAllHouse(self):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT * FROM rumah
            """
        )

        data = curr.fetchall()
        
        conn.commit()
        curr.close()
        conn.close()   

        return data

    
