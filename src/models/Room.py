import sqlite3
class Room :
    def __init__(self, nama : str, rumah_id : int, powerCap : int) :
        self.id:int
        self.nama : str = nama
        self.rumah_id : int = rumah_id
        self.powerCap = powerCap

        conn = sqlite3.connect('db/wireWolf.db')
        addCircuitBreaker = conn.cursor()

        addCircuitBreaker.execute(
            """
            INSERT INTO circuit_breaker(kapasitas_daya) 
            VALUES ({0})
            """
            .format(self.powerCap)
        )
        addCircuitBreaker.close()

        
        findIdCircuitBreaker=conn.cursor()
        findIdCircuitBreaker.execute(
            """
            SELECT *
            FROM circuit_breaker
            ORDER BY id DESC
            LIMIT 1
            """
        )

        data = findIdCircuitBreaker.fetchall()
        circuitID=data[0][0]
        self.id_circuitBreaker=circuitID
        findIdCircuitBreaker.close()

        addRoom=conn.cursor()
        addRoom.execute(
            """
            INSERT INTO  ruangan(nama, id_rumah, id_circuit)
            VALUES ('{0}', {1}, {2})
            """
            .format(nama, rumah_id, circuitID)
        )
        addRoom.close()
        
        conn.commit()
        conn.close()

    @classmethod
    def getRoomById(cls, idRoom:int):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
                SELECT * 
                FROM ruangan
                WHERE id={0}
            """
            .format(idRoom)
        )
        data = curr.fetchall()
        
        self = cls.__new__(cls)
        if(len(data) > 0):
            id, nama, rumah_id, id_circuit = data[0]
            self.id = id 
            self.nama = nama
            self.rumah_id = rumah_id
            self.id_circuitBreaker = id_circuit
        else:
            self.id = ""
            self.nama = ""
            self.rumah_id = ""
            self.id_circuitBreaker = ""

        curr.execute(
            """
                SELECT * 
                FROM circuit_breaker
                WHERE id = {0}
            """
            .format(self.id_circuitBreaker)
        )
        data = curr.fetchall()

        if(len(data)>0):
            self.powerCap = data[0][1]
        else:
            self.powerCap = 0
        curr.close()
        conn.close()      

        return self
    
    def setRoom(self,Name:str, ID:int) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE Ruangan
            SET nama = '{0}'
            WHERE id = {1}
            """
            .format(Name, ID)
        )

    
    def addElectricity(self,nama:str, daya:int, voltase:int, waktu_penggunaan ) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            INSERT INTO  alat_listrik(nama, ruangan_id, daya, voltase, waktu_penggunaan)
            VALUES ('{0}', {1}, {2}, {3}, {4})
            """
            .format(nama,self.id, daya, voltase, waktu_penggunaan)
        )
    
    def removeRoom(self) :
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            DELETE FROM alat_listrik
            WHERE ruangan_id = {0}
            """
            .format(self.id)
        )
        curr.execute(
            """
            DELETE FROM circuit_breaker
            WHERE id = {0}
            """
            .format(self.id_circuitBreaker)
        )
        curr.execute(
            """
            DELETE FROM ruangan
            WHERE id = {0}
            """
            .format(self.id)
        )
        curr.close()
        conn.commit()
        conn.close()
    
    def removeElectricity(self) :
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            DELETE FROM alat_listrik
            WHERE ruangan_id = {0}
            """
            .format(self.id)
        )
    
    def getElectricity(self) :
        conn=sqlite3.connect('db/wirewolf.db')
        curr=conn.cursor()
        curr.execute(
            """
            SELECT *
            FROM alat_listrik
            WHERE ruangan_id = {0}
            """
            .format(self.id)
        )
        data=curr.fetchall()
        return data

