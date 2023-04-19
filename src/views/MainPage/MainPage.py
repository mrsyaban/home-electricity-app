from PyQt5.QtWidgets import *
from views.MainPage.HouseItem import HouseItem
from views.MainPage.Dialog.AddHouseDialog import AddHouseDialog
from models.HouseManager import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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

        # logoFrame
        self.logoFrame = QFrame()
        self.logoFrame.setMaximumSize(QSize(16777215, 300))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.logoFrame.setObjectName("logoFrame")

        self.logoLayout = QVBoxLayout(self.logoFrame)
        self.logoWidget = QWidget(self.logoFrame)
        self.logo = QLabel(self.logoWidget)
        logoPixmap = QPixmap(f"{getDirPath()}/src/assets/logo.png").scaled(400, 200)
        self.logo.setPixmap(logoPixmap)
        self.logo.setAlignment(Qt.AlignHCenter)
        self.logoLayout.addWidget(self.logo)
        self.logoLayout.setContentsMargins(0, 30, 0, 0)

        # --- Body Frame ---
        self.bodyFrame = QFrame()
        self.bodyFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Raised)
        self.bodyLayout = QVBoxLayout(self.bodyFrame)
        self.bodyLayout.setContentsMargins(250,0,250,0)

        # -- List Title Frame --
        self.titleFrame = QFrame(self.bodyFrame)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.titleLayout = QHBoxLayout(self.titleFrame)
        self.titleLayout.setContentsMargins(20,0,20,0)

        # label
        self.label = QLabel("Daftar Rumah ", self.titleFrame)
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        
        # add Button
        self.addButton = QPushButton()
        self.addButton.setStyleSheet( "QPushButton { background-color: rgba(0,0,0,0); border-radius:12px}\n"
                            "QPushButton::hover  { background-color: #999999;}\n")
        plusIcon = QIcon(f"{getDirPath()}/src/assets/Plus.png")
        plusSize = plusIcon.actualSize(QSize(50, 50))
        self.addButton.setIcon(plusIcon)
        self.addButton.setIconSize(plusSize)
        self.addButton.setFixedSize(plusSize)

        self.addButton.clicked.connect(self.handleClick)

        self.titleLayout.addWidget(self.label)
        self.titleLayout.addWidget(self.addButton)
        
        # -- List House Frame --
        self.listFrame = QFrame(self.bodyFrame)
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.listLayout = QVBoxLayout(self.listFrame)


        for i in range(len(self.listHouse)):
            item = HouseItem(self.parent, str(self.listHouse[i][0]), self.listHouse[i][1], self)
            self.listLayout.addWidget(item)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.listLayout.addItem(spacerItem)

        self.bodyLayout.addWidget(self.titleFrame)
        self.bodyLayout.addWidget(self.listFrame)
        self.Layout.addWidget(self.logoFrame)
        self.Layout.addWidget(self.bodyFrame)
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
        self.listFrame.deleteLater()

        self.getDB()

        self.listFrame = QFrame(self.bodyFrame)
        self.listFrame.setFrameShape(QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QFrame.Raised)
        self.listLayout = QVBoxLayout(self.listFrame)
        self.bodyLayout.addWidget(self.listFrame)

        for i in range(len(self.listHouse)):
            item = HouseItem(self.parent, str(self.listHouse[i][0]), self.listHouse[i][1], self)
            self.listLayout.addWidget(item)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.listLayout.addItem(spacerItem)

        self.Layout.addWidget(self.bodyFrame)
