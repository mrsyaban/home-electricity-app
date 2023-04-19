from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from views.HouseManager.RoomItem import RoomItem
from models.House import *
from models.CircuitBreaker import *
from models.Room import *

class ListRoom(QWidget):
    def __init__(self, parent: QWidget, scrollArea: QWidget, idHouse: str, mode: bool, grandPa):
        super().__init__()
        self.parent = parent
        self.idHouse = idHouse
        self.mode = mode
        self.grandPa = grandPa
        self.listRoom = []
        self.listCap = []
        self.listCntEl = []
        self.getDB()
        self.initUI(scrollArea)

    def initUI(self, scrollArea: QWidget):
        self.layout = QGridLayout(scrollArea)
        for i in range(len(self.listRoom)):
                room = RoomItem(str(self.listRoom[i][0]), self.listRoom[i][1], self.listCntEl[i], self.listCap[i], self.parent, self.mode, self.grandPa)
                self.layout.addWidget(room, i//2, i%2)

        self.setLayout(self.layout)

    def getDB(self):
        if(self.idHouse != "-1"):
            dataHouse = House.getHouseById(self.idHouse)
            listRoom = dataHouse.getAllRoom()
            listCap = []
            listCntEl = []
            for i in range(len(listRoom)):
                tmpCap = CircuitBreaker.getCircuitBreakerById(listRoom[i][3]).getCapacity()
                listCap.append(tmpCap)
                room = Room.getRoomById(listRoom[i][0])
                listCntEl.append(len(room.getElectricity()))

            self.listRoom = listRoom
            self.listCap = listCap
            self.listCntEl = listCntEl