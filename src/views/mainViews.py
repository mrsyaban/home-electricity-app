from PyQt5.QtWidgets import QStackedWidget , QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from MainPage.MainPage import MainPage
from HousePage.HousePage import HousePage

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.mainPage: QWidget = MainPage(self)
        self.housePage: QWidget = HousePage(self, "-1")
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle("Routing Pages")
        self.addWidget(self.mainPage)
        self.addWidget(self.housePage)
        self.show()

    def setIdHouse(self, id: str):
        newHousePage: HousePage = HousePage(self, id)
        self.housePage = newHousePage
        self.addWidget(newHousePage)
        self.setCurrentWidget(self.housePage)