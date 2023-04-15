import models.Room as Room

class RoomController:
    def add(nama : str,rumah_id : int, voltase : int, cnt_room : int, isSimulate : bool, id_circuitBreaker : int):
        try:
            Room.Room(nama,rumah_id, voltase, cnt_room, isSimulate, id_circuitBreaker)
        except:
            print("Gagal menambahkan ruangan")
    def ubahNamaRuangan(id,nama):
        try:
            Room.Room.setRoom(nama,id)
        except:
            print("Gagal mengubah nama ruangan")
    def addElectricRoom(nama:str, daya:int, voltase:int, waktu_penggunaan,id:int ):
        try:
            ubah = Room.Room.getRoomById(id)
            ubah.addElectricity(nama,daya,voltase,waktu_penggunaan)
        except:
            print("Gagal menambahkan elektronik")
    def removeRoom(id):
        try:
            ambil = Room.Room.getRoomById(id)
            ambil.removeRoom()
        except:
            print("Gagal menghapus ruangan")
    