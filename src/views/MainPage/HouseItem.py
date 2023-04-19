from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget, QHBoxLayout, QLabel
from controller.houseController import *
from views.MainPage.Button.houseListButton import HouseButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from utils.getDirPath import getDirPath
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

        # houseName
        self.houseButton = HouseButton(self.nama, f"{getDirPath()}/src/assets/right.png")

        #delete Button
        self.delButton = QPushButton()
        self.delButton.setStyleSheet("QPushButton{background-color: rgba(0,0,0,0); border-radius:12px;}\n"
                                     "QPushButton::hover  { background-color: #999999;}\n")
        icon = QIcon(f"{getDirPath()}/src/assets/Delete.png")
        icon_size = icon.actualSize(QSize(70, 70))
        self.delButton.setIcon(icon)
        self.delButton.setIconSize(icon_size)
        self.delButton.setFixedSize(icon_size)
        self.delButton.clicked.connect(self.handleClickDel)
        self.houseButton.clicked.connect(self.handleClickShow)

        self.layout.addWidget(self.houseButton)
        self.layout.addWidget(self.delButton)
        self.setLayout(self.layout)
    
    def handleClickShow(self: QWidget):
        self.grandPa.setIdHouse(self.id)

    def handleClickDel(self: QWidget):
        houseController = HouseController()
        houseController.removehouse(self.id)
        self.parent.reload()