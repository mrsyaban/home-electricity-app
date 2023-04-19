from PyQt5.QtWidgets import QStackedWidget , QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from views.HouseManager.HousePage.HousePage import HousePage
# from views.HouseManager.SimulationPage.SimulationPage import SimulationPage
from models.Room import *
from models.House import *

class HouseManager(QStackedWidget):
    def __init__(self, parent: QStackedWidget, id: str):
        super().__init__()
        self.id = id
        self.parent = parent
        self.isSimulate = False
        self.createState()
        self.housePage: QWidget = HousePage(self, self.id, self.parent)
        # self.simulationPage: QWidget = SimulationPage(self, self.id, self.parent)
        self.initUI()

    def initUI(self):
        self.addWidget(self.housePage)
        # self.addWidget(self.simulationPage)
        self.setCurrentWidget(self.housePage)
        self.show()

    def setMode(self):
        self.isSimulate = not self.isSimulate
        if(self.isSimulate):
            self.createState()
            # self.setCurrentWidget(self.simulationPage)
        else:
            self.setCurrentWidget(self.housePage)

    def reload(self):
        self.removeWidget(self.housePage)
        self.housePage = HousePage(self, self.id, self.parent)
        self.addWidget(self.housePage)
        self.setCurrentWidget(self.housePage)

    def createState(self):
        if(self.id != "-1"):
            self.elsState = {}
            house = House.getHouseById(self.id)
            listRoom = house.getAllRoom()
            for i in range(len(listRoom)):
                tmpEl = []
                room = Room.getRoomById(listRoom[i][0])
                listEl = room.getElectricity()
                for j in range(len(listEl)):
                    tmpEl.append(False)
                self.elsState[str(listRoom[i][0])] = tmpEl

    def setState(self, idRoom, idx, value):
        self.elsState[idRoom][idx] = value
        # self.simulationPage.reloadUI()
