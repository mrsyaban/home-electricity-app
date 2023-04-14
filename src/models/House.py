import sqlite3

class House :
    # CONSTRUCTOR
    def __init__(self, name, power) :
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
    def getHouseById(cls, idHouse):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
                SELECT * 
                FROM rumah
                WHERE id={idHouse}
            """
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

    def addRoom():
        #something


    
