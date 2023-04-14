from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel, QVBoxLayout, QPushButton
from MainPage.HouseItem import HouseItem

class MainPage(QWidget):
    def __init__(self, parent: QStackedWidget):
        super().__init__()
        self.parent: QStackedWidget = parent
        self.initUI()

    def initUI(self):
        self.layout: QVBoxLayout = QVBoxLayout()
        self.title: QLabel = QLabel("Daftar Rumah")

        self.layout.addWidget(self.title)
        for i in range(4):
            label = HouseItem(self.parent, str(i), str(i+1))
            label.clicked.connect(label.handleClick)
            self.layout.addWidget(label)

        self.setLayout(self.layout)

        self.setLayout(self.layout)