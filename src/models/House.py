import sqlite3

class House :
    # CONSTRUCTOR
    def __init__(self, name:str, power:int) :
        self.id:int
        self.name:str = name 
        self.power:int = power
        self.idCircuit:int

        conn = sqlite3.connect('habibi.db')
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
        print(circuitId)
        
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
        conn = sqlite3.connect('habibi.db')
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
        print(data)
        houseId, houseName, circuitId = data[0]

        self = cls.__new__(cls)
        self.id = houseId 
        self.name = houseName
        self.idCircuit = circuitId

        curr.close()
        conn.close()      

        return self

    def editHouseName(self, newName:str):
        conn = sqlite3.connect('habibi.db')
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
        conn = sqlite3.connect('habibi.db')
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
        conn = sqlite3.connect('habibi.db')
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