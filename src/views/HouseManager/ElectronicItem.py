from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models.Electronic import *
from utils.getDirPath import getDirPath
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon


class ElectronicItem(QFrame):
    def __init__(self, id: str, parent: QStackedWidget, nama: str, isInSimulation: bool, grandPa1, idRoom: str, idx: int, herit):
        super().__init__(herit)
        self.id: str = id
        self.nama: str = nama
        self.parent: str = parent
        self.isInSimulation: bool = isInSimulation
        self.grandPa1 = grandPa1
        self.idRoom = idRoom
        self.idx = idx
        self.initUI()

    def initUI(self):
        # electronic item

        self.itemLayout = QHBoxLayout(self)
        self.itemLayout.setContentsMargins(0, 0, 0, 0)
        self.itemLayout.setSpacing(3)
        
        self.itemName = QPushButton(self)
        self.itemName.setText(self.nama) #input item Name
        self.itemLayout.addWidget(self.itemName) 

        self.setMinimumSize(QSize(0, 40))
        self.setMaximumSize(QSize(16777215, 40))
        self.setStyleSheet("background-color: #D9D9D9;\n"
                                     "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                     "border-radius: 20px;\n"
                                     "padding: 5px;\n"
                                     "padding-left: 15px;\n"
                                     "padding-right: 15px;\n"
                                     "color: \'#000000\';\n"
                                     "")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        if (self.isInSimulation):
            self.checkBox = QCheckBox(self)
            self.checkBox.setChecked(False)
            self.checkBox.setMaximumSize(QtCore.QSize(40, 16777215))
            if(self.grandPa1.elsState[self.idRoom][self.idx]):
                self.checkBox.setChecked(True)
                self.checkBox.clicked.connect(self.handleToggle)
            self.itemLayout.addWidget(self.checkBox)
            self.checkBox.clicked.connect(self.handleToggle)
        else:
            self.delButton = QPushButton(self)
            self.delButton.setStyleSheet("QPushButton{background-color: rgba(0,0,0,0); border-radius:12px;}\n"
                                     "QPushButton::hover  { background-color: #999999;}\n")
            icon = QIcon(f"{getDirPath()}/src/assets/Delete.png")
            icon_size = icon.actualSize(QtCore.QSize(70, 70))
            self.delButton.setIcon(icon)
            self.delButton.setIconSize(icon_size)
            self.delButton.setFixedSize(icon_size)
            self.delButton.clicked.connect(self.handleDelete)
            self.itemLayout.addWidget(self.delButton)

        self.setLayout(self.itemLayout)

    def handleToggle(self):
        self.grandPa1.setState(self.idRoom, self.idx, self.checkBox.isChecked()) 

    def handleDelete(self):
        electronic = Electronic.getElectronicById(int(self.id))
        electronic.deleteElectronic()
        self.grandPa1.reload()
