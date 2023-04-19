from PyQt5.QtWidgets import *
from views.MainPage.HouseItem import HouseItem
from views.MainPage.Dialog.AddHouseDialog import AddHouseDialog
from models.HouseManager import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from utils.getDirPath import getDirPath

class MainPage(QWidget):
    def __init__(self, parent: QStackedWidget):
        super().__init__()
        self.parent: QStackedWidget = parent
        self.listHouse = []
        self.getDB()
        self.initUI()

    def initUI(self):
        self.Layout: QVBoxLayout = QVBoxLayout()
        self.logo = QLabel()
        self.midWidget = QWidget()
        self.Layout.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(f"{getDirPath()}/img/logo.png")
        original_width = pixmap.width()
        original_height = pixmap.height()
        new_width = 400
        new_height = int((new_width / original_width) * original_height)
        new_pixmap = pixmap.scaled(new_width, new_height)
        self.logo.setPixmap(new_pixmap)

        self.Layout.addWidget(self.logo)
        
        midLayout = QHBoxLayout()
        label: QLabel = QLabel("Daftar Rumah")
        label.setStyleSheet("font-weight: 600; font-size: 28px;")
        addButton = QPushButton()
        buttonPixmap = QPixmap(f"{getDirPath()}/img/plus.png")
        addButton.setIcon(QIcon(buttonPixmap))
        addButton.setFixedWidth(40)
        addButton.setStyleSheet("background-color: rgba(0,0,0,0);")
        addButton.clicked.connect(self.handleClick)
        
        midLayout.addWidget(label)
        midLayout.addWidget(addButton)
        self.midWidget.setLayout(midLayout)
        self.midWidget.setMaximumWidth(500)

        self.Layout.addWidget(self.midWidget)

        self.listWidget = QWidget()
        layoutList = QVBoxLayout()

        for i in range(len(self.listHouse)):
            item = HouseItem(self.parent, str(self.listHouse[i][0]), self.listHouse[i][1], self)
            layoutList.addWidget(item)

        self.listWidget.setLayout(layoutList)
        self.Layout.addWidget(self.listWidget)
        self.setLayout(self.Layout)

    def getDB(self):
        houseManager = HouseManager()
        data = houseManager.getAllHouse()
        if(len(data)>0):
            self.listHouse = data

    def handleClick(self):
        dialog = AddHouseDialog(self)
        dialog.exec_()

    def reload(self):
        self.listWidget.deleteLater()

        self.getDB()

        self.listWidget = QWidget()
        layoutList = QVBoxLayout()

        for i in range(len(self.listHouse)):
            item = HouseItem(self.parent, str(self.listHouse[i][0]), self.listHouse[i][1], self)
            layoutList.addWidget(item)

        self.listWidget.setLayout(layoutList)
        self.Layout.addWidget(self.listWidget)
