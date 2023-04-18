from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from views.HouseManager.Dialog.AddRoomDialog import *

class CntRoomLabel(QWidget):
    def __init__(self, cntRoom: int, idHouse: str, mode: bool):
        super().__init__()
        self.idHouse: str = idHouse
        self.mode: bool = mode
        self.cntRoom: int = cntRoom
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.widgetLabel = QWidget()
        self.layoutLabel  = QVBoxLayout()
        self.label = QLabel("Jumlah Ruangan")
        self.value = QLabel(str(self.cntRoom))

        self.layoutLabel.addWidget(self.label)
        self.layoutLabel.addWidget(self.value)

        self.widgetLabel.setLayout(self.layoutLabel)
        self.layout.addWidget(self.widgetLabel)
        if(not self.mode):
            self.addRoomButton = QPushButton("+")
            self.addRoomButton.clicked.connect(self.handleClick)
            self.layout.addWidget(self.addRoomButton)

        self.setLayout(self.layout)

    def handleClick(self):
        addRoomDialog = AddRoomDialog(self.idHouse)
        addRoomDialog.exec_()
