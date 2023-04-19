from PyQt5.QtWidgets import QLabel, QSpacerItem, QPushButton,QVBoxLayout, QWidget, QFrame, QSizePolicy, QStackedWidget, QHBoxLayout
from views.HouseManager.BackButton import BackButton
from views.HouseManager.Labels.CntRoomLabel import CntRoomLabel
from views.HouseManager.Labels.PowHouseLabel import PowHouseLabel
from views.HouseManager.Labels.ConsumeLabel import ConsumeLabel
from models.House import *
from models.CircuitBreaker import *
from PyQt5 import QtCore, QtGui
from views.HouseManager.Dialog.AddRoomDialog import *
from models.Room import Room
from utils.getDirPath import *


class DetailHouse(QWidget):
    def __init__(self, grandPa: QStackedWidget, id: str, grandPa1: QStackedWidget, mode: bool):
        super().__init__()
        self.id: str = id
        self.grandPa: QWidget = grandPa
        self.grandPa1: QStackedWidget = grandPa1
        self.mode: bool = mode
        self.title = "Dummy Title"
        self.cntRoom = 0
        self.powerCap = 0
        self.elConsume = 0
        self.isOn = False
        self.changeIsOn()
        self.getDB()
        self.initUI()

    def initUI(self):
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(153, 0))
        self.setMaximumSize(QtCore.QSize(308, 16777215))
        self.setStyleSheet("")
        # self.setObjectName("sideBar")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.houseInfo = QFrame(self)
        self.houseInfo.setMinimumSize(QtCore.QSize(0, 330))
        self.houseInfo.setMaximumSize(QtCore.QSize(16777215, 500))
        self.houseInfo.setFrameShape(QFrame.StyledPanel)
        self.houseInfo.setFrameShadow(QFrame.Raised)
        self.houseInfo.setObjectName("houseInfo")
        self.verticalLayout_4 = QVBoxLayout(self.houseInfo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.houseTitle = QFrame(self.houseInfo)
        self.houseTitle.setMinimumSize(QtCore.QSize(0, 72))
        self.houseTitle.setMaximumSize(QtCore.QSize(16777215, 72))
        self.houseTitle.setObjectName("houseTitle")
        self.horizontalLayout_4 = QHBoxLayout(self.houseTitle)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backButton = BackButton(self.grandPa1)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_4.addWidget(self.backButton)
        self.houseName = QLabel(self.houseTitle)
        self.houseName.setMinimumSize(QtCore.QSize(60, 15))
        self.houseName.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.houseName.setFont(font)
        self.houseName.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.houseName.setObjectName("houseName")
        self.horizontalLayout_4.addWidget(self.houseName)
        self.verticalLayout_4.addWidget(self.houseTitle)
        self.numRoom = QFrame(self.houseInfo)
        self.numRoom.setMinimumSize(QtCore.QSize(0, 72))
        self.numRoom.setMaximumSize(QtCore.QSize(16777215, 72))
        self.numRoom.setObjectName("numRoom")
        self.horizontalLayout_5 = QHBoxLayout(self.numRoom)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_9 = QWidget(self.numRoom)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 72))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 72))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_2 = QVBoxLayout(self.widget_9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QLabel(self.widget_9)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.widget_9)
        self.plusButton = QPushButton(self.numRoom)
        self.plusButton.setStyleSheet('background-color: transparent; border-style: none;')
        icon = QIcon(f'{getDirPath()}/src/assets/plus.png')
        icon_size = icon.actualSize(QSize(100, 100)) # 70 is the maximum size in pixels
        self.plusButton.setIcon(icon)
        self.plusButton.setIconSize(icon_size)
        self.plusButton.setFixedSize(icon_size)
        self.plusButton.clicked.connect(self.handleClickAddRoom)
        self.plusButton.setMinimumSize(QtCore.QSize(52, 52))
        self.plusButton.setMaximumSize(QtCore.QSize(52, 52))
        self.plusButton.setObjectName("plusButton")
        self.horizontalLayout_5.addWidget(self.plusButton)
        self.verticalLayout_4.addWidget(self.numRoom)

        self.capacity = QFrame(self.houseInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capacity.sizePolicy().hasHeightForWidth())
        self.capacity.setSizePolicy(sizePolicy)
        self.capacity.setMinimumSize(QtCore.QSize(0, 72))
        self.capacity.setMaximumSize(QtCore.QSize(16777215, 72))
        self.capacity.setObjectName("capacity")
        self.horizontalLayout_7 = QHBoxLayout(self.capacity)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_11 = QWidget(self.capacity)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 72))
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_5 = QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QLabel(self.widget_11)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QLabel(self.widget_11)
        self.label_7.setMinimumSize(QtCore.QSize(0, 10))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_7.addWidget(self.widget_11)
        self.verticalLayout_4.addWidget(self.capacity)

        self.consum = QFrame(self.houseInfo)
        self.consum.setMinimumSize(QtCore.QSize(0, 72))
        self.consum.setMaximumSize(QtCore.QSize(16777215, 72))
        self.consum.setFrameShape(QFrame.StyledPanel)
        self.consum.setFrameShadow(QFrame.Raised)
        self.consum.setObjectName("consum")
        self.verticalLayout_6 = QVBoxLayout(self.consum)
        self.verticalLayout_6.setContentsMargins(12, 3, 12, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QLabel(self.consum)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_9 = QLabel(self.consum)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.verticalLayout_4.addWidget(self.consum)

        self.status = QFrame(self.houseInfo)
        self.status.setMinimumSize(QtCore.QSize(0, 72))
        self.status.setMaximumSize(QtCore.QSize(16777215, 72))
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setFrameShadow(QFrame.Raised)
        self.status.setObjectName("status")
        self.verticalLayout_7 = QVBoxLayout(self.status)
        self.verticalLayout_7.setContentsMargins(12, 3, 12, 3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QLabel(self.status)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.label_11 = QLabel(self.status)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.verticalLayout_4.addWidget(self.status)

        self.verticalLayout.addWidget(self.houseInfo)
        spacerItem = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.runButton = QFrame(self)
        self.runButton.setMinimumSize(QtCore.QSize(0, 70))
        self.runButton.setMaximumSize(QtCore.QSize(16777215, 80))
        self.runButton.setObjectName("runButton")
        self.verticalLayout_7 = QVBoxLayout(self.runButton)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_3 = QPushButton(self.runButton)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.handleClick)
        self.verticalLayout_7.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.runButton)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        # self.horizontalLayout.addWidget(self)
        self.retranslateUi(self.grandPa)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StackedWidget"))
        self.houseName.setText(_translate("MainWindow", self.title))
        self.label_2.setText(_translate("MainWindow", "Jumlah Ruangan"))
        self.label.setText(_translate("MainWindow", str(self.cntRoom)))
        self.label_6.setText(_translate("MainWindow", "Kapasitas"))
        self.label_7.setText(_translate("MainWindow", f"{self.powerCap} Watt"))
        self.label_8.setText(_translate("MainWindow", "Konsumsi Daya"))
        self.label_9.setText(_translate("MainWindow", f"{self.elConsume} Watt"))
        if(self.mode):
            self.pushButton_3.setText(_translate("MainWindow", "Stop"))
            self.pushButton_3.setStyleSheet("padding: 6px; background-color: #CA1313; border-style: none; border-radius: 8px; color: white; font-size: 14px;")
            self.label_10.setText(_translate("MainWindow", "Status"))
            self.label_11.setText(_translate("MainWindow", "Mati"))
            if(self.isOn):
                self.label_11.setText(_translate("MainWindow", "Hidup"))
        else:
            self.pushButton_3.setText(_translate("MainWindow", "Run"))
            self.pushButton_3.setStyleSheet("padding: 6px; background-color: #00A027; border-style: none; border-radius: 8px; color: white; font-size: 14px;")

    def handleClick(self):
        self.grandPa.setMode()

    def handleClickAddRoom(self):
        addRoomDialog = AddRoomDialog(self.id, self.grandPa)
        addRoomDialog.exec_()

    def getDB(self):
        if(self.id != "-1"):
            dataHouse = House.getHouseById(self.id)
            dataCircuit = CircuitBreaker.getCircuitBreakerById(dataHouse.idCircuit)
            
            listRoom = dataHouse.getAllRoom()
            tmpConsume = 0
            for i in range(len(listRoom)):
                room = Room.getRoomById(listRoom[i][0])
                listEl = room.getElectricity()
                for j in range(len(listEl)):
                    tmpConsume += listEl[j][3]*listEl[j][5]*30
            
            self.title = dataHouse.name
            self.powerCap = dataCircuit.getCapacity()
            self.cntRoom = len(listRoom)
            self.elConsume = tmpConsume

    def changeIsOn(self):
        if(self.id != "-1"):
            if(self.mode):
                tmpPower = 0
                house = House.getHouseById(self.id)
                listRoom = house.getAllRoom()
                for i in range(len(listRoom)):
                    room = Room.getRoomById(listRoom[i][0])
                    listEl = room.getElectricity()
                    for j in range(len(listEl)):
                        if(self.grandPa.elsState[str(listRoom[i][0])][j]):
                            tmpPower += listEl[j][3]
                            
                if(tmpPower>house.power):
                    self.isOn = True
