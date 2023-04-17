
from models.Electronic import Electronic
import sqlite3

class ElectronicController:
    def addElectricRoom(id_ruangan: int, nama : str, daya : int, voltase : int, waktu : int, detail : str, isOn : bool = True):
        try:
            Electronic.Electronic(id_ruangan, nama, daya, voltase, waktu, detail, isOn)
        except:
            print("Gagal menambahkan elektronik")
    def removeElectricRoom(id):
        try:
            conn = sqlite3.connect('db/wirewolf.db')
            curr = conn.cursor()

            curr.execute(
                """
                DELETE FROM elektronik WHERE id = {0}
                """
                .format(id)
            )

            curr.close()
            conn.close()
        except:
            print("Gagal menghapus elektronik")
    def ubahNamaElektronik(id,nama):
        try:
            ubah = Electronic.Electronic.getElectronicById(id)
            ubah.setName(nama)
        except:
            print("Gagal mengubah nama elektronik")
    def ubahWattElektronik(id,daya):
        try:
            ubah = Electronic.Electronic.getElectronicById(id)
            ubah.setWatt(daya)
        except:
            print("Gagal mengubah watt elektronik")
    def ubahDetailElektronik(id,detail):
        try:
            ubah = Electronic.Electronic.getElectronicById(id)
            ubah.setDetail(detail)
        except:
            print("Gagal mengubah detail elektronik")
    def ubahVoltaseElektronik(id,voltase):
        try:
            ubah = Electronic.Electronic.getElectronicById(id)
            ubah.setVoltase(voltase)
        except:
            print("Gagal mengubah voltase elektronik")
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
        simpanid = []
        for i in range(len(ans)):
            simpanid.append(ans[i][0])
        return simpanid