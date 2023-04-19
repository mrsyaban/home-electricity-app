from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from views.HouseManager.ElectronicItem import *
from views.HouseManager.Dialog.AddElectronicDialog import *

class DetailRoom(QWidget):
    def __init__(self, parent: QWidget, idRoom: str, mode: bool):
        super().__init__()
        self.idRoom: str = idRoom
        self.mode: bool = mode
        self.parent: QWidget = parent
        self.initUI()

    def initUI(self):
        # self.layout = QVBoxLayout()

        # self.labelName = QLabel(self.idRoom)

        # self.layout.addWidget(self.labelName)
        # if(not self.mode):
        #     self.addButton = QPushButton("+")
        #     self.addButton.clicked.connect(self.handleAdd)
        #     self.layout.addWidget(self.addButton)
        # for i in range(4):
        #     label = ElectronicItem(self, "Electronic " + str(i), self.mode)
        #     self.layout.addWidget(label)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(9, 50, 9, -1)
        
        self.titleHolds = QWidget(self)
        self.titleLayout = QVBoxLayout(self.titleHolds)

        # room title
        self.roomTitle = QPushButton(self.titleHolds)
        self.roomTitle.setText("Ruangan Coli") #input title 
        font = QFont()
        font.setPointSize(20)
        self.roomTitle.setFont(font)
        self.roomCap = QPushButton(self.titleHolds)
        self.roomCap.setText("1000 Megawati") #input roomcap

        self.titleLayout.addWidget(self.roomTitle)
        self.titleLayout.addWidget(self.roomCap)

        self.layout.addWidget(self.titleHolds, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: \'#98ABC8\';\n"
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
"    background-color: \'#707070\';\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color:\'#707070\';\n"
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 535, 518))
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)

        # body layout (add button and items)
        self.body = QWidget(self.scrollAreaWidgetContents)
        self.body.setMinimumSize(QtCore.QSize(0, 500))
        self.body.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.bodyLayout = QVBoxLayout(self.body)
        # self.bodyLayout.setContentsMargins(100, -1, 100, -1)

        # addButton
        self.addElec = QPushButton(self.body)
        self.addElec.setText("+")
        self.addElec.setMinimumSize(QtCore.QSize(0, 40))
        self.addElec.setStyleSheet("QPushButton {background-color: #D9D9D9;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;}\n"
"QPushButton::hover { background-color: #565656;}\n")
        
        self.bodyLayout.addWidget(self.addElec)

        # Frame for list item
        self.listItemFrame = QFrame(self.body)
        self.listItemLayout = QVBoxLayout(self.listItemFrame)

        # electronic item
        self.itemFrame = QFrame(self.listItemFrame)
        self.itemFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.itemFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.itemFrame.setStyleSheet("background-color: #D9D9D9;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: \'#000000\';\n"
"")
        self.itemFrame.setFrameShape(QFrame.StyledPanel)
        self.itemFrame.setFrameShadow(QFrame.Raised)
        self.itemLayout = QHBoxLayout(self.itemFrame)
        self.itemLayout.setContentsMargins(0, 0, 0, 0)
        self.itemLayout.setSpacing(3)
        
        self.itemName = QPushButton(self.itemFrame)
        self.itemName.setText("") #input item Name
        self.checkBox = QCheckBox(self.itemFrame)
        self.checkBox.setMaximumSize(QtCore.QSize(40, 16777215))

        self.itemLayout.addWidget(self.itemName)
        self.itemLayout.addWidget(self.checkBox)
        self.bodyLayout.addWidget(self.itemFrame)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.listItemLayout.addItem(spacerItem)

        self.bodyLayout.addWidget(self.listItemFrame)

        self.scrollLayout.addWidget(self.body)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        
        self.setLayout(self.layout)

    def handleAdd(self):
        dialog = AddElectronicDialog()
        dialog.exec_()
