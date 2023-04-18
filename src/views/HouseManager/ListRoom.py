from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from views.HouseManager.RoomItem import RoomItem

class ListRoom(QWidget):
    def __init__(self, parent: QWidget, scrollArea: QWidget, idHouse: str, mode: bool):
        super().__init__()
        self.parent = parent
        self.idHouse = idHouse
        self.mode = mode
        self.initUI(scrollArea)

    def initUI(self, scrollArea: QWidget):
        self.layout = QGridLayout(scrollArea)
        for i in range(2):
            for j in range(2):
                room = RoomItem(str(i+j), str(i+j+1), 10+1, 1000+100*i+j*50, self.parent, self.mode)
                self.layout.addWidget(room, i, j)

        self.setLayout(self.layout)