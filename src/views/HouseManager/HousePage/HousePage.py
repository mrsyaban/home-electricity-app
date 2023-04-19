from PyQt5.QtWidgets import QFrame, QAbstractScrollArea, QWidget, QStackedWidget, QSizePolicy,QLabel, QHBoxLayout, QScrollArea, QVBoxLayout
from views.HouseManager.ListRoom import ListRoom
from views.HouseManager.DetailHouse import DetailHouse
# from views.HouseManager.DetailRoom import DetailRoom
from PyQt5 import QtCore

class HousePage(QWidget):
    def __init__(self, parent: QStackedWidget, idHouse: str, grandPa: QStackedWidget):
        super().__init__()
        self.id: str = idHouse
        self.idRoom: str = "-1"
        self.parent = parent
        self.grandPa: QStackedWidget = grandPa
        self.initUI()

    def initUI(self):
        self.layout: QHBoxLayout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.detailHouse = DetailHouse(self.parent, self.id, self.grandPa, False)
        # self.detailRoom: DetailRoom = DetailRoom(self, self.idRoom, False)

        self.roomSpace = QWidget(self.parent)
        self.roomSpace.setEnabled(False)
        self.roomSpace.setMinimumSize(QtCore.QSize(461, 432))
        self.roomSpace.setStyleSheet("background-color: \"#D9D9D9\";\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.roomSpace.setObjectName("roomSpace")

        self.horizontalLayout_3 = QHBoxLayout(self.roomSpace)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.scrollArea_2 = QScrollArea(self.roomSpace)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 432))
        self.scrollArea_2.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: \'#d9d9d9\';\n"
"    width: 12px;\n"
"    margin: 20px 0 20px 0;\n"
"    border-radius: 5px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: \'#a1a1a1\';\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: \'#696969\';\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: none;\n"
"    height: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"")
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 260, 1518))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.horizontalLayout_3.addWidget(self.scrollArea_2)

        self.layout.addWidget(self.detailHouse)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)

        # frame for detail room
        self.detailRoomSpace = QFrame(self.roomSpace)
        self.detailRoomSpace.setMaximumSize(QtCore.QSize(308, 16777215))
        self.detailRoomSpace.setStyleSheet("background-color: \"#98ABC8\";\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.detailRoomSpace.setObjectName("detailRoomSpace")
        self.verticalLayout_3 = QVBoxLayout(self.detailRoomSpace)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # self.verticalLayout_3.addWidget(self.detailRoom)
        self.horizontalLayout_3.addWidget(self.detailRoomSpace)
        self.layout.addWidget(self.roomSpace)

        self.listRoom: ListRoom = ListRoom(self, self.scrollAreaWidgetContents_2, self.id, False)
        self.gridLayout_2.addWidget(self.listRoom)
        # self.layout.addWidget(self.listRoom)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # self.layout.addWidget(self.detailRoom)
        self.setLayout(self.layout)

    def setIdRoom(self, idRoom):
        self.idRoom = idRoom
        newDetailRoom: DetailRoom = DetailRoom(self, self.idRoom, False)
        self.layout.removeWidget(self.detailRoom)
        self.layout.addWidget(newDetailRoom)
        self.detailRoom = newDetailRoom

