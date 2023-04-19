from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from views.HouseManager.ElectronicItem import *
from views.HouseManager.Dialog.AddElectronicDialog import *
from models.Room import *

class DetailRoom(QWidget):
    def __init__(self, parent: QWidget, idRoom: str, mode: bool, grandPa):
        super().__init__()
        self.idRoom: str = idRoom
        self.mode: bool = mode
        self.parent: QWidget = parent
        self.grandPa = grandPa
        self.room = {}
        self.listElectronic = []
        self.getDB()
        self.initUI()

    def initUI(self):
        if(self.idRoom != "-1"):
            self.layout = QVBoxLayout()
            self.labelName = QLabel(self.room.nama)

            self.layout.addWidget(self.labelName)
            if(not self.mode):
                self.addButton = QPushButton("+")
                self.addButton.clicked.connect(self.handleAdd)
                self.layout.addWidget(self.addButton)
            for i in range(len(self.listElectronic)):
                label = ElectronicItem(self.listElectronic[i][0], self, self.listElectronic[i][1], self.mode, self.grandPa, self.idRoom, i)
                self.layout.addWidget(label)

            self.setLayout(self.layout)

    def getDB(self):
        if(self.idRoom != "-1"):
            room = Room.getRoomById(self.idRoom)
            listElectronic = room.getElectricity()
            self.room = room
            self.listElectronic = listElectronic

    def handleAdd(self):
        dialog = AddElectronicDialog(self.idRoom, self.grandPa)
        dialog.exec_()
