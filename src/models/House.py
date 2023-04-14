import sqlite3

class House :
    # CONSTRUCTOR
    def __init__(self, name:str, power:int) :
        self.id:int
        self.name:str = name 
        self.power:int = power
        self.idCircuit:int

        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            INSERT INTO circuit_breaker(kapasitas_daya)
            VALUE ({0})
            """
            .format(power)
        )

        curr.execute(
            """
            SELECT id 
            FROM circuit_breaker
            ORDER BY id
            LIMIT 1
            """
        )

        circuitId = curr.fetchall()
        
        curr.execute(
            """
            INSERT INTO rumah(nama, id_circuit)
            VALUE ({0}, {1})
            """
            .format(name, circuitId)
        )

        curr.close()
        conn.close()


    # CONSTRUCTOR BY ID
    @classmethod
    def getHouseById(cls, idHouse:int):
        conn = sqlite3.connect('db/wirewolf.db')
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
        houseId, houseName, housePower, circuitId = data

        self = cls.__new__(cls)
        self.id = houseId 
        self.name = houseName
        self.power = housePower
        self.idCircuit = circuitId

        curr.close()
        conn.close()      

        return self

    def editHouseName(self, newName:str):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE rumah
            SET nama = {0}
            WHERE id = {1}
            """
            .format(newName, self.id)
        )

        curr.close()
        conn.close()      
    
    def editPowerCap(self, newPower:int):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE circuit_breaker
            SET kapasitas_daya = {0}
            WHERE id = {1}
            """
            .format(newPower, self.idCircuit)
        )

        curr.close()
        conn.close()      

    def deleteHouse(self):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            DELETE FROM rumah
            WHERE id = {0}
            """
            .format(self.id)
        )

        curr.close()
        conn.close()

    

    
