from PyQt5.QtWidgets import QFrame, QAbstractScrollArea, QWidget, QStackedWidget, QSizePolicy,QLabel, QHBoxLayout, QScrollArea, QVBoxLayout
from views.HouseManager.ListRoom import ListRoom
from views.HouseManager.DetailHouse import DetailHouse
from views.HouseManager.DetailRoom import DetailRoom
from PyQt5 import QtCore

class SimulationPage(QWidget):
    def __init__(self, parent: QStackedWidget, idHouse: str, grandPa: QStackedWidget):
        super().__init__()
        self.id: str = idHouse
        self.idRoom: str = "-1"
        self.parent = parent
        self.grandPa: QStackedWidget = grandPa
        self.initUI()

    def initUI(self):
        self.layout: QHBoxLayout = QHBoxLayout()
        self.detailHouse = DetailHouse(self.parent, self.id, self.grandPa, True)
        self.listRoom: ListRoom = ListRoom(self, self.id, True, self.parent)
        self.detailRoom: DetailRoom = DetailRoom(self, self.idRoom, True, self.parent)
        self.detailHouse.setMaximumWidth(300)

        self.layout.addWidget(self.detailHouse)

        self.scrollArea_2 = QScrollArea()

        self.scrollArea_2.setStyleSheet("background-color: white; border-radius: 20px;")
        self.scrollArea_2.setWidget(self.listRoom)

        self.layout.addWidget(self.scrollArea_2)
        self.layout.addWidget(self.detailRoom)
        self.scrollArea_2.setWidgetResizable(True)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)
        self.setLayout(self.layout)

    def setIdRoom(self, idRoom):
        self.idRoom = idRoom
        newDetailRoom: DetailRoom = DetailRoom(self, self.idRoom, True, self.parent)
        self.layout.removeWidget(self.detailRoom)
        self.layout.addWidget(newDetailRoom)
        self.detailRoom = newDetailRoom
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)

    def reloadUI(self):
        newDetailHouse = DetailHouse(self.parent, self.id, self.grandPa, True)
        newListRoom = ListRoom(self, self.id, True, self.parent)
        newDetailRoom = DetailRoom(self, self.idRoom, True, self.parent)
        newScroll = QScrollArea()

        self.detailHouse.deleteLater()
        self.scrollArea_2.deleteLater()
        self.detailRoom.deleteLater()

        newScroll.setStyleSheet("background-color: white; border-radius: 20px;")
        newScroll.setWidget(newListRoom)
        newScroll.setWidgetResizable(True)

        self.scrollArea_2 = newScroll

        self.detailHouse = newDetailHouse
        self.listRoom = newListRoom
        self.detailRoom = newDetailRoom

        self.layout.addWidget(self.detailHouse)
        self.layout.addWidget(self.scrollArea_2)
        self.layout.addWidget(self.detailRoom)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)

