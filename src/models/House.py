import sqlite3

class House :
    # CONSTRUCTOR
    def __init__(self, name:str, power:int) :
        self.id:int
        self.name:str = name 
        self.power:int = power
        self.idCircuit:int

        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            INSERT INTO circuit_breaker(kapasitas_daya)
            VALUES ({0})
            """
            .format(power)
        )

        conn.commit()

        curr.execute(
            """
            SELECT id 
            FROM circuit_breaker
            ORDER BY id DESC
            LIMIT 1
            """
        )

        circuitId = curr.fetchall()[0][0]
        curr.execute(
            """
            INSERT INTO rumah(nama, id_circuit)
            VALUES ('{0}', {1})
            """
            .format(name, circuitId)
        )
        conn.commit()
        curr.close()
        conn.close()


    # CONSTRUCTOR BY ID
    @classmethod
    def getHouseById(cls, idHouse:int):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
                SELECT * 
                FROM rumah
                WHERE id={0}
            """
            .format(idHouse)
        )
        data = curr.fetchall()
        self = cls.__new__(cls)
        if(len(data) > 0):
            houseId, houseName, circuitId = data[0]
            self.id = houseId 
            self.name = houseName
            self.idCircuit = circuitId
        else:
            self.id = ""
            self.name = ""
            self.idCircuit = ""

        curr.close()
        conn.close()      

        return self

    def editHouseName(self, newName:str):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE rumah
            SET nama = '{0}'
            WHERE id = {1}
            """
            .format(newName, self.id)
        )
        
        conn.commit()
        curr.close()
        conn.close()      
    
    def editPowerCap(self, newPower:int):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE circuit_breaker
            SET kapasitas_daya = {0}
            WHERE id = {1}
            """
            .format(newPower, self.idCircuit)
        )

        conn.commit()
        curr.close()
        conn.close()      

    def deleteHouse(self):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            DELETE FROM rumah
            WHERE id = {0}
            """
            .format(self.id)
        )
        
        conn.commit()
        curr.close()
        conn.close()

    def getAllRoom(self):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT *
            FROM ruangan
            WHERE id_rumah = {0}
            """
            .format(self.id)
        )

        data = curr.fetchall()
        
        conn.commit()
        curr.close()
        conn.close()

        return data