import models.Room as Room
import sqlite3

class ElectronicController:
    def addElectricRoom(nama:str, daya:int, voltase:int, waktu_penggunaan,id:int ):
        try:
            ubah = Room.Room.getRoomById(id)
            ubah.addElectricity(nama,daya,voltase,waktu_penggunaan)
        except:
            print("Gagal menambahkan elektronik")
    def removeElectricRoom(id):
        try:
            ambil = Room.Room.getRoomById(id)
            ambil.removeElectricity()
        except:
            print("Gagal menghapus elektronik")
    def getListElectricRoom(id):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT id FROM elektronik WHERE id_ruang = {0}
            """
            .format(id)
        )
        ans = curr.fetchall()
        curr.close()
        conn.close()
        return ans