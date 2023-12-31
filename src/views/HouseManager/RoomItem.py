from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton,QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from models.Room import *
from utils.getDirPath import *

class RoomItem(QWidget):
    def __init__(self, id: str, name: str, cntEl: int, powerCap: int, grandPa: QWidget, mode: bool, grandPa1):
        super().__init__()
        self.id = id
        self.name = name
        self.cntEl = cntEl
        self.powerCap = powerCap
        self.grandPa = grandPa
        self.mode = mode
        self.grandPa1 = grandPa1
        self.isOn = False
        self.changeIsOn()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 200, 300))
        self.widget.setStyleSheet("QWidget { background-color: \'#FEF7F7\';}")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.roomTitle_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        self.roomTitle_2.setFont(font)
        self.roomTitle_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.roomTitle_2.setAutoFillBackground(False)
        self.roomTitle_2.setStyleSheet("font: 20pt \"Arial\";")
        self.roomTitle_2.setScaledContents(True)
        self.roomTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.roomTitle_2.setWordWrap(False)
        self.roomTitle_2.setObjectName("roomTitle_2")
        self.verticalLayout_5.addWidget(self.roomTitle_2)
        self.numElectronic_2 = QtWidgets.QFrame(self.widget)
        self.numElectronic_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.numElectronic_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numElectronic_2.setObjectName("numElectronic_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.numElectronic_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.numElectronic_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_5.addWidget(self.numElectronic_2)
        self.powerCap_2 = QtWidgets.QFrame(self.widget)
        self.powerCap_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.powerCap_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.powerCap_2.setObjectName("powerCap_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.powerCap_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.powerCap_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(68, 68, 68);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_4.addWidget(self.widget_5)
        self.verticalLayout_5.addWidget(self.powerCap_2)

        self.retranslateUi(Form)

        if(self.mode):
            self.indicator = QLabel("mati")
            self.indicator.setMaximumSize(50,50)
            self.indicator.setMinimumSize(50,50)
            self.indicator.setText("")
            self.indicator.setFixedHeight(30)
            self.indicator.setStyleSheet("margin: 0 10px 0 10px; padding: 6px; background-color: black; border-style: none; border-radius: 15px; color: white; font-size: 14px;")
            if(self.isOn):
                self.indicator.setStyleSheet("margin: 0 10px 0 10px; padding: 6px; background-color: yellow; border-style: none; border-radius: 15px; color: white; font-size: 14px;")
            self.verticalLayout_5.addWidget(self.indicator)
        else:
            self.deletButton_2 = QtWidgets.QPushButton(self.widget)
            self.deletButton_2.setStyleSheet('QPushButton { background-color: transparent; border-radius: 7px;} QPushButton::hover { background-color: #999999;}')
            icon = QIcon(f'{getDirPath()}/src/assets/Delete.png')
            icon_size = icon.actualSize(QSize(100, 100))
            self.deletButton_2.setIcon(icon)
            self.deletButton_2.setIconSize(icon_size)
            self.deletButton_2.setFixedSize(icon_size)
            self.deletButton_2.setObjectName("deletButton_2")
            self.deletButton_2.clicked.connect(self.handleClickDel)
            self.verticalLayout_5.addWidget(self.deletButton_2, 0, QtCore.Qt.AlignCenter)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roomTitle_2.setText(_translate("Form", self.name))
        self.label_5.setText(_translate("Form", "Jumlah Perangkat "))
        self.label_6.setText(_translate("Form", f"{self.cntEl}"))
        self.label_7.setText(_translate("Form", "Kapasitas Daya"))
        self.label_8.setText(_translate("Form", f"{self.powerCap} Watt"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.grandPa.setIdRoom(self.id)

    def handleClickDel(self):
        room = Room.getRoomById(self.id)
        room.removeRoom()
        self.grandPa1.reload()

    def changeIsOn(self):
        if(self.mode):
            tmpPower = 0
            room = Room.getRoomById(self.id)
            listEl = room.getElectricity()
            for i in range(len(listEl)):
                if(self.grandPa1.elsState[self.id][i]):
                    tmpPower += listEl[i][3]

            if(tmpPower>self.powerCap):
                self.isOn = True