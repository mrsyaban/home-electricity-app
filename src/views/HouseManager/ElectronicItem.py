from PyQt5.QtWidgets import QPushButton, QStackedWidget, QWidget, QHBoxLayout, QLabel
from models.Electronic import *

class ElectronicItem(QWidget):
    def __init__(self, id: str, parent: QStackedWidget, nama : str, isInSimulation : bool, grandPa1, idRoom: str, idx: int):
        super().__init__()
        self.id: str = id
        self.nama: str = nama
        self.parent: str = parent
        self.isInSimulation : bool = isInSimulation
        self.grandPa1 = grandPa1
        self.idRoom = idRoom
        self.idx = idx
        self.initUI()

    def initUI(self):
        self.layout: QHBoxLayout = QHBoxLayout()
        self.label : QLabel = QLabel(self.nama)
        if (self.isInSimulation):
            self.button : QPushButton = QPushButton("Off")
            self.button.setCheckable(True)
            self.button.setChecked(False)
            if(self.grandPa1.elsState[self.idRoom][self.idx]):
                    self.button.setText("On")
                    self.button.setChecked(True)
            self.button.clicked.connect(self.handleToggle)

        else:
            self.button : QPushButton = QPushButton("Delete")
            self.button.clicked.connect(self.handleDelete)


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def handleToggle(self):
        self.grandPa1.setState(self.idRoom, self.idx, self.button.isChecked())
        if (self.button.isChecked()):
            self.button.setText("On")
        else:
            self.button.setText("Off")

    def handleDelete(self):
        electronic = Electronic.getElectronicById(int(self.id))
        electronic.deleteElectronic()
        self.grandPa1.reload()
