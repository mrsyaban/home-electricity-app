import models.Room as Room
import sqlite3
class RoomController:
    def add(nama : str, rumah_id : int, power : int):
        try:
            Room.Room(nama,rumah_id,power)
        except:
            print("Gagal menambahkan ruangan")
    def ubahNamaRuangan(id,nama):
        try:
            Room.Room.setRoom(nama,id)
        except:
            print("Gagal mengubah nama ruangan")
    def removeRoom(id):
        try:
            ambil = Room.Room.getRoomById(id)
            ambil.removeRoom()
        except:
            print("Gagal menghapus ruangan")
    def getAllRoom(id):
        conn = sqlite3.connect('db/wirewolf.db')
        curr = conn.cursor()
        curr.execute(
            """
            SELECT id FROM ruangan WHERE id_rumah = {0}
            """
            .format(id)
        )
        ans = curr.fetchall()
        curr.close()
        conn.close()
        simpan = []
        for i in ans:
            simpan.append(i[0])
        return simpan
    