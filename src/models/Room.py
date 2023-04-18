import sqlite3
class Room :
    def __init__(self, nama : str, rumah_id : int, power : int, isSimulate : bool) :
        self.id:int
        self.nama : str = nama
        self.rumah_id : int = rumah_id
        self.isSimulate : bool = isSimulate
        self.id_circuitBreaker : int 
        self.power:int = power
        
        conn = sqlite3.connect('db/wireWolf.db')
        addCircuitBreaker = conn.cursor()

        addCircuitBreaker.execute(
            """
            INSERT INTO circuit_breaker(kapasitas_daya) 
            VALUES ({0})
            """
            .format(power)
        )
        addCircuitBreaker.close()

        
        findIdCircuitBreaker=conn.cursor()
        findIdCircuitBreaker.execute(
            """
            SELECT id
            FROM circuit_breaker
            ORDER BY id DESC
            LIMIT 1
            """
        )

        circuitID=findIdCircuitBreaker.fetchall()[0][0]
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

        findIdRoom=conn.cursor()
        findIdRoom.execute(
            """
            SELECT id
            FROM ruangan
            ORDER BY id DESC
            LIMIT 1
            """
        )
        self.id=findIdRoom.fetchall()[0][0]
        findIdRoom.close()
    
        
        conn.commit()
        conn.close()
    @classmethod
    def getRoomById(cls,id:int) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT *
            FROM ruangan
            WHERE id = {0}
            """
            .format(id)
        )

        data = curr.fetchall()
        findPower=conn.cursor()
        findPower.execute(
            """
            SELECT kapasitas_daya
            FROM circuit_breaker
            WHERE id = {0}
            """
            .format(data[0][3])
        )

        self=cls.__new__(cls)
        self.id:int=data[0][0]
        self.nama : str = data[0][1]
        self.rumah_id : int = data[0][2]
        self.isSimulate : bool = False #default
        self.id_circuitBreaker : int = data[0][3]
        self.power:int = findPower.fetchall()[0][0]

        findPower.close()
        curr.close()
        conn.close()

        return self
    
    def editRoomName(self,Name:str) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE Ruangan
            SET nama = '{0}'
            WHERE id = {1}
            """
            .format(Name, self.id)
        )
        self.nama=Name
        curr.close()
        conn.commit()
        conn.close()
    
    def editPowerCap(self,newPower:int) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            UPDATE circuit_breaker
            SET kapasitas_daya = {0}
            WHERE id = {1}
            """
            .format(newPower, self.id_circuitBreaker)
        )
        self.power=newPower
        curr.close()
        conn.commit()
        conn.close()
    
    def deleteRoom(self) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            DELETE FROM Ruangan
            WHERE id = {0}
            """
            .format(self.id)
        )
        self.id=0
        self.nama="Deleted"
        self.rumah_id=0
        self.isSimulate=False
        self.id_circuitBreaker=0
        self.power=0

        curr.close()
        conn.commit()
        conn.close()
    
    def getAllElectricityID(self) :
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            SELECT id
            FROM alat_listrik
            WHERE ruangan_id = {0}
            """
            .format(self.id)
        )

        data = curr.fetchall()

        result=[]

        for i in data :
            result.append(i[0])

        curr.close()
        conn.close()
        return result
    
    def getManyElectricity(self):
        conn=sqlite3.connect('db/wireWolf.db')
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

        return len(data)

