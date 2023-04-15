import sqlite3
class Room :
    def __init__(self, nama : str, rumah_id : int, voltase : int, isSimulate : bool) :
        self.id:int
        self.nama : str = nama
        self.rumah_id : int = rumah_id
        self.isSimulate : bool = isSimulate
        self.id_circuitBreaker : int 

        conn = sqlite3.connect('gui/wireWolf.db')
        addCircuitBreaker = conn.cursor()

        addCircuitBreaker.execute(
            """
            INSERT INTO circuit_breaker(kapasitas_daya) 
            VALUES ({0})
            """
            .format(voltase)
        )
        addCircuitBreaker.close()

        
        findIdCircuitBreaker=conn.cursor()
        findIdCircuitBreaker.execute(
            """
            SELECT id
            FROM circuit_breaker
            ORDER BY id 
            LIMIT 1
            """
        )

        circuitID=findIdCircuitBreaker.fetchall()[0][0]
        self.id_circuitBreaker=circuitID
        findIdCircuitBreaker.close()

        addRoom=conn.cursor()
        addRoom.execute(
            """
            INSERT INTO  ruangan(nama, rumah_id, id_circuit)
            VALUES ('{0}', {1}, {2})
            """
            .format(nama, rumah_id, circuitID)
        )
        addRoom.close()

        findIdRoom=conn.cursor()
        findIdRoom.execute(
            """
            SELECT id
            FROM ruangan
            ORDER BY id 
            LIMIT 1
            """
        )
        self.id=findIdRoom.fetchall()[0][0]
        findIdRoom.close()
    
        
        conn.commit()
        conn.close()

    @staticmethod
    def setRoom(self,Name:str, ID:int) :
        conn = sqlite3.connect('gui/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE Ruangan
            SET nama = '{0}'
            WHERE id = {1}
            """
            .format(Name, ID)
        )

    @staticmethod
    def addElectricity(self,nama:str, daya:int, voltase:int, waktu_penggunaan ) :
        conn = sqlite3.connect('gui/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            INSERT INTO  alat_listrik(nama, ruangan_id, daya, voltase, waktu_penggunaan)
            VALUES ('{0}', {1}, {2}, {3}, {4})
            """
            .format(nama,self.id, daya, voltase, waktu_penggunaan)
        )

    @staticmethod
    def getRoomById(self,id:int) :
        conn = sqlite3.connect('gui/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT *
            FROM Ruangan
            WHERE id = {0}
            """
            .format(id)
        )

        data = curr.fetchone()
        return data
 