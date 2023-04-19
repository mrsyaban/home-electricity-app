from PyQt5.QtWidgets import QStackedWidget , QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from views.MainPage.MainPage import MainPage
# from views.HouseManager.HouseManager import *

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.mainPage: QWidget = MainPage(self)
        # self.houseManager: QWidget = HouseManager(self, "-1")
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle("Wire Wolf")
        self.setStyleSheet("background-color: #98ABC8;")
        self.addWidget(self.mainPage)
        # self.addWidget(self.houseManager)
        self.show()

    # def setIdHouse(self, id: str):
        # newHouseManager: HouseManager = HouseManager(self, id)
        # self.houseManager = newHouseManager
        # self.addWidget(newHouseManager)
        # self.setCurrentWidget(self.houseManager)
        
    def back(self):
        self.setCurrentWidget(self.mainPage)