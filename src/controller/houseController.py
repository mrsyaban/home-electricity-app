import models.House as House
class HouseController:
    def add(self,nama : str,power : int):
        try:
            House(nama,power)
        except:
            print("Gagal menambahkan rumah")
    def removehouse(self,id):
        try:
            ambil = House.getHouseById(id)
            ambil.deleteHouse()
        except:
            print("Gagal menghapus rumah")
    def renameHouse(self,id,nama):
        try:
            ambil = House.getHouseById(id)
            ambil.editHouseName(nama)
        except:
            print("Gagal mengubah nama rumah")
    def changePower(self,id,power):
        try:
            ambil = House.getHouseById(id)
            ambil.editPowerCap(power)
        except:
            print("Gagal mengubah kapasitas daya")
    def getHouse(self,id):
        return House.getHouseById(id)
    
