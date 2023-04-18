import sqlite3

class CircuitBreaker:
    def __init__(self, kapasitasDaya):
        self.__kapasitasDaya = kapasitasDaya
        self.__status = False
        conn = sqlite3.connect('db/wireWolf.db')
        c = conn.cursor()
        c.execute(
            """
            Insert into CircuitBreaker (kapasitas_day) values ({0})
            """.format(kapasitasDaya)
        )

        c.execute(
            """
            SELECT id 
            FROM CircuitBreaker 
            ORDER BY id DESC 
            LIMIT 1
            """
        )
        self.__id = c.fetchone()[0]
        c.close()
        conn.close()
        
    @classmethod
    def getCircuitBreakerById(cls, circuitBreakerID:int):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
                SELECT * 
                FROM CircuitBreaker
                WHERE id={0}
            """
            .format(circuitBreakerID)
        )
        data = curr.fetchall()
        circuitBreakerID, kapasitasDaya = data

        self = cls.__new__(cls)
        self.__id = circuitBreakerID
        self.__kapasitasDaya = kapasitasDaya

        curr.close()
        conn.close()      

        return self

    def getCapacity(self):
        return self.__kapasitasDaya
    
    def getID(self):
        return self.__id

    def getStatus(self):
        return self.__status

    def setCapacity(self, kapasitasDaya):
        self.__kapasitasDaya = kapasitasDaya
        conn = sqlite3.connect('db/wireWolf.db')
        c = conn.cursor()
        c.execute(
            """
            UPDATE CircuitBreaker SET kapasitas_day = {0}
            WHERE id = {1}
            """.format(kapasitasDaya, self.__id)
        )
        c.close()
        conn.close()

    def on(self):
        self.__status = True

    def off(self):
        self.__status = False

