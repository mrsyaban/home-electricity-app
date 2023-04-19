from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from views.HouseManager.ElectronicItem import *
from views.HouseManager.Dialog.AddElectronicDialog import *
from views.HouseManager.ElectronicItem import *
from models.Room import *
from models.Room import Room
from controller.electronicController import ElectronicController


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
        if (self.idRoom != "-1"):
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(9, 50, 9, -1)

            self.titleHolds = QWidget(self)
            self.titleLayout = QVBoxLayout(self.titleHolds)

        # room title
            self.roomTitle = QPushButton(self.titleHolds)
            self.roomTitle.setText(self.room.nama)  # input title
            self.roomTitle.setStyleSheet(
                'background-color: transparent; border-style: none;')
            font = QFont()
            font.setPointSize(20)
            self.roomTitle.setFont(font)

            roomPowerCap = self.room.powerCap
            self.roomCap = QPushButton(self.titleHolds)
            self.roomCap.setText(str(roomPowerCap))  # input roomcap
            self.roomCap.setStyleSheet(
                'background-color: transparent; border-style: none;')

            self.titleLayout.addWidget(self.roomTitle)
            self.titleLayout.addWidget(self.roomCap)

            self.layout.addWidget(self.titleHolds, 0, QtCore.Qt.AlignHCenter)
            self.scrollArea = QScrollArea(self)
            self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
                                        "    border: none;\n"
                                        "    background-color: \'#98ABC8\';\n"
                                        "    width: 12px;\n"
                                        "    margin: 20px 0 20px 0;\n"
                                        "    border-radius: 5px;\n"
                                        " }\n"
                                        "\n"
                                        "/*  HANDLE BAR VERTICAL */\n"
                                        "QScrollBar::handle:vertical {    \n"
                                        "    background-color: \'#a1a1a1\';\n"
                                        "    min-height: 30px;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover{    \n"
                                        "    background-color: \'#707070\';\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:pressed {    \n"
                                        "    background-color:\'#707070\';\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN TOP - SCROLLBAR */\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "    border: none;\n"
                                        "    background-color: none;\n"
                                        "    height: 15px;\n"
                                        "    border-top-left-radius: 4px;\n"
                                        "    border-top-right-radius: 4px;\n"
                                        "    subcontrol-position: top;\n"
                                        "    subcontrol-origin: margin;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical:hover {    \n"
                                        "    background-color: rgb(255, 0, 127);\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:pressed {    \n"
                                        "    background-color: rgb(185, 0, 92);\n"
                                        "}\n"
                                        "")
            self.scrollArea.setWidgetResizable(True)
            self.scrollAreaWidgetContents = QWidget()
            self.scrollAreaWidgetContents.setGeometry(
                QtCore.QRect(0, 0, 535, 518))
            self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)

            # body layout (add button and items)
            self.body = QWidget(self.scrollAreaWidgetContents)
            self.body.setMinimumSize(QtCore.QSize(0, 500))
            self.body.setMaximumSize(QtCore.QSize(16777215, 1000))
            self.bodyLayout = QVBoxLayout(self.body)
            # self.bodyLayout.setContentsMargins(100, -1, 100, -1)

            # addButton
            self.addElec = QPushButton(self.body)
            self.addElec.clicked.connect(self.handleAdd)
            self.addElec.setText("+")
            self.addElec.setMinimumSize(QtCore.QSize(0, 40))
            self.addElec.setStyleSheet("QPushButton {background-color: #D9D9D9;\n"
                                    "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                    "border-radius: 20px;\n"
                                        "padding: 5px;\n"
                                    "padding-left: 15px;\n"
                                        "padding-right: 15px;}\n"
                                        "QPushButton::hover { background-color: #565656;}\n")

            self.bodyLayout.addWidget(self.addElec)

            # Frame for list item
            self.listItemFrame = QFrame(self.body)
            self.listItemLayout = QVBoxLayout(self.listItemFrame)

            for i in range(len(self.listElectronic)):
                # electronic item
                self.item = ElectronicItem(
                    self.listElectronic[i][0], self, self.listElectronic[i][1], self.mode, self.grandPa, self.idRoom, i, self.listItemFrame)

                self.bodyLayout.addWidget(self.item)

                spacerItem = QSpacerItem(
                    20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                self.listItemLayout.addItem(spacerItem)

            self.bodyLayout.addWidget(self.listItemFrame)

            self.scrollLayout.addWidget(self.body)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.layout.addWidget(self.scrollArea)

            self.setLayout(self.layout)

    def handleAdd(self):
        dialog = AddElectronicDialog(self.idRoom, self.grandPa)
        dialog.exec_()

    def getDB(self):
        if (self.idRoom != "-1"):
            room = Room.getRoomById(self.idRoom)
            listElectronic = room.getElectricity()
            self.room = room
            self.listElectronic = listElectronic
