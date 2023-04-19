from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget, QHBoxLayout, QLabel
from controller.houseController import *

class HouseItem(QWidget):
    def __init__(self, grandPa: QStackedWidget, id: str, nama: str, parent):
        super().__init__()
        self.id: str = id
        self.nama: str = nama
        self.grandPa: str = grandPa
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.label = QLabel(self.nama)
        self.delButton = QPushButton("del")
        self.delButton.clicked.connect(self.handleClickDel)
        self.showButton = QPushButton("show")
        self.showButton.clicked.connect(self.handleClickShow)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.delButton)
        self.layout.addWidget(self.showButton)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #D9D9D9;\nfont: 75 8pt \"MS Shell Dlg 2\";\nborder-radius: 20px;\npadding: 5px;\npadding-left: 15px;\npadding-right: 15px;\ncolor: '#000000';")

    def handleClickShow(self: QWidget):
        self.grandPa.setIdHouse(self.id)

    def handleClickDel(self: QWidget):
        houseController = HouseController()
        houseController.removehouse(self.id)
        self.parent.reload()