import sqlite3
# class House:
#     def __init__(self,nama,voltase):
#         self.nama = nama
#         self.volt = voltase
#     def getName(self):
#         return self.nama
#     def getVolt(self):
#         return self.volt
#     def __str__(self):
#         return "Rumah "+self.nama+" berkapasitas "+str(self.volt)
class HouseManager:
    def __init__(self, listHome : list):
        self.listHome : list = listHome
    def add(self,nama,voltase):
        House(nama,voltase)#nanti 
    def removehouse(self,no):
        buang = self.listHome.pop(no-1)
    def getID(self,no):
        return self.listHome[no-1][0]
    def renameHouse(self,no,nama):
        self.listHome[no-1] = nama
        idubah = self.getID(no)
        conn = sqlite3.connect("../db/wireWolf.db")
        curr = conn.cursor()
        sql_command = """UPDATE rumah SET nama = {0} WHERE id = {1};""".format(nama,idubah)
        curr.execute(sql_command)
        conn.commit()
        conn.close()
    def getListHouse(self):
        conn = sqlite3.connect("../db/wireWolf.db")
        curr = conn.cursor()
        sql_command = """SELECT id, nama FROM rumah;"""
        curr.execute(sql_command)
        ans = curr.fetchall()
        conn.commit()
        conn.close()
        return ans
    def getHouse(self,no):
        return self.listHome[no-1]
    def getHouseList(self):
        return self.listHome
