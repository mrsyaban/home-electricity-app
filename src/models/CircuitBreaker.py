import sqlite3

class CircuitBreaker:
    def __init__(self, kapasitasDaya):
        self.__kapasitasDaya = kapasitasDaya
        self.__status = False
        conn = sqlite3.connect('db/wireWolf.db')
        c = conn.cursor()
        c.execute(
            """
            Insert into circuit_breaker (kapasitas_day) values ({0})
            """.format(kapasitasDaya)
        )

        c.execute(
            """
            SELECT id 
            FROM circuit_breaker 
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
                FROM circuit_breaker
                WHERE id={0}
            """
            .format(circuitBreakerID)
        )
        data = curr.fetchall()
        self = cls.__new__(cls)
        if(len(data)>0):
            circuitBreakerID, kapasitasDaya = data[0]

            self.__id = circuitBreakerID
            self.__kapasitasDaya = kapasitasDaya
        else:
            self.__id = ""
            self.__kapasitasDaya = 0

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
            UPDATE circuit_breaker SET kapasitas_day = {0}
            WHERE id = {1}
            """.format(kapasitasDaya, self.__id)
        )
        c.close()
        conn.close()

    def on(self):
        self.__status = True

    def off(self):
        self.__status = False

