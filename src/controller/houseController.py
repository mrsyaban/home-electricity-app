import models.House as House
import sqlite3
class HouseController:
    def add(self,nama : str,power : int):
        try:
            House(nama,power)
        except:
            print("Gagal menambahkan rumah")
    def removehouse(self,id):
        try:
            ambil = House.House.getHouseById(id)
            ambil.deleteHouse()
        except:
            print("Gagal menghapus rumah")
    def renameHouse(self,id,nama):
        try:
            ambil = House.House.getHouseById(id)
            ambil.editHouseName(nama)
        except:
            print("Gagal mengubah nama rumah")
    def changePower(self,id,power):
        try:
            ambil = House.House.getHouseById(id)
            ambil.editPowerCap(power)
        except:
            print("Gagal mengubah kapasitas daya")
    def getHouse(self,id):
        return House.getHouseById(id)
    def getAllHouse(self):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()

        curr.execute(
            """
            SELECT * FROM rumah
            """
            .format(self.id)
        )
        ans = curr.fetchall()
        curr.close()
        conn.close()
        return ans

    
