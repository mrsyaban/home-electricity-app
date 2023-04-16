import sqlite3

class Electronic :
    def __init__(self, id_ruangan: int, nama : str, daya : int, voltase : int, waktu : int, detail : str, isOn : bool = True) :
        self.__nama : str = nama
        self.__daya : int = daya
        self.__voltase : int = voltase
        self.__waktu : int = waktu
        self.__detail : str = detail
        self.__isOn : bool = isOn
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            INSERT INTO alat_listrik(nama, ruangan_id, daya, voltase, waktu, detail)
            VALUE ('{0}',{1},{2},{3},{4},'{5}')
            """
            .format(nama,id_ruangan,daya,voltase,waktu,detail)
        )

        curr.execute(
            """
            SELECT id 
            FROM alat_listrik
            ORDER BY id
            LIMIT 1
            """
        )

        self.__id = curr.fetchone()
    

        curr.close()
        conn.close()

    @classmethod
    def getElectronicById(cls, electronicID:int):
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()

        curr.execute(
            """
                SELECT * 
                FROM alat_listrik
                WHERE id={0}
            """
            .format(electronicID)
        )
        data = curr.fetchall()
        if len(data) == 0 :
            return None
        
        nama = data[1]
        daya = data[3]
        voltase = data[4]
        waktu = data[5]
        detail = data[6]

        self = cls.__new__(cls)
        self.__id = electronicID
        self.__nama = nama
        self.__daya = daya
        self.__voltase = voltase
        self.__waktu = waktu
        self.__detail = detail
        self.__isOn = True

        curr.close()
        conn.close()      

        return self

    def setName(self, nama : str):
        self.__nama = nama
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            UPDATE alat_listrik
            SET nama = '{0}'
            WHERE id = {1}
            """
            .format(nama,self.__id)
        )
        curr.close()
        conn.close()

    def setWatt(self, daya : int):
        self.__daya = daya
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            UPDATE alat_listrik
            SET daya = {0}
            WHERE id = {1}
            """
            .format(daya,self.__id)
        )
        curr.close()
        conn.close()
    
    def setDetail(self, detail : str):
        self.__detail = detail
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            UPDATE alat_listrik
            SET detail = '{0}'
            WHERE id = {1}
            """
            .format(detail,self.__id)
        )
        curr.close()
        conn.close()

    def setVoltase(self, voltase : int):
        self.__voltase = voltase
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            UPDATE alat_listrik
            SET voltase = {0}
            WHERE id = {1}
            """
            .format(voltase,self.__id)
        )
        curr.close()
        conn.close()

    def setWaktu(self, waktu : int):
        self.__waktu = waktu
        conn = sqlite3.connect('db/wireWolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            UPDATE alat_listrik
            SET waktu = {0}
            WHERE id = {1}
            """
            .format(waktu,self.__id)
        )
        curr.close()
        conn.close()

    def getName(self) :
        return self.__nama
    
    def getWatt(self) :
        return self.__daya
    
    def getDetail(self) :
        return self.__detail
    
    def getVoltase(self) :
        return self.__voltase
    
    def getWaktu(self) :
        return self.__waktu
    
    def getIsOn(self) :
        return self.__isOn

    def on(self) :
        self.__isOn = True

    def off(self) :
        self.__isOn = False

    
