from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models.Electronic import *


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
        # self.layout: QHBoxLayout = QHBoxLayout()
        # self.label : QLabel = QLabel(self.nama)
        # if (self.isInSimulation):
        #     self.button : QPushButton = QPushButton("Off")
        #     self.button.setCheckable(True)
        #     self.button.setChecked(False)
        #     if(self.grandPa1.elsState[self.idRoom][self.idx]):
        #             self.button.setText("On")
        #             self.button.setChecked(True)
        #     self.button.clicked.connect(self.handleToggle)

        # else:
        #     self.button : QPushButton = QPushButton("Delete")
        #     self.button.clicked.connect(self.handleDelete)
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
        self.itemLayout = QHBoxLayout(self)
        self.itemLayout.setContentsMargins(0, 0, 0, 0)
        self.itemLayout.setSpacing(3)

        self.itemName = QPushButton(self)
        self.itemName.setText(self.nama)

        self.itemLayout.addWidget(self.itemName)
        if (self.isInSimulation):
            self.buttonCheckBox: QPushButton = QPushButton("Off")
            self.buttonCheckBox.setCheckable(True)
            self.buttonCheckBox.setChecked(False)
            if (self.grandPa1.elsState[self.idRoom][self.idx]):
                self.buttonCheckBox.setText("On")
                self.buttonCheckBox.setChecked(True)
            self.itemLayout.addWidget(self.buttonCheckBox)
            self.buttonCheckBox.clicked.connect(self.handleToggle)
        else:
            self.buttonDel : QPushButton = QPushButton("Delete")
            self.buttonDel.clicked.connect(self.handleDelete)
            self.itemLayout.addWidget(self.buttonDel)

    def handleToggle(self):
        self.grandPa1.setState(self.idRoom, self.idx, self.buttonCheckBox.isChecked())
        if (self.buttonCheckBox.isChecked()):
            self.buttonCheckBox.setText("On")
        else:
            self.buttonCheckBox.setText("Off")

    def handleDelete(self):
        electronic = Electronic.getElectronicById(int(self.id))
        electronic.deleteElectronic()
        self.grandPa1.reload()
