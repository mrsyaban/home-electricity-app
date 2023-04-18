from PyQt5.QtWidgets import QPushButton, QStackedWidget

class HouseItem(QPushButton):
    def __init__(self, grandPa: QStackedWidget, id: str, nama: str):
        super().__init__()
        self.id: str = id
        self.nama: str = nama
        self.grandPa: str = grandPa
        self.initUI()

    def initUI(self):
        self.setText(self.nama)

    def handleClick(self: QPushButton):
        self.grandPa.setIdHouse(self.id)
        self.grandPa.setCurrentWidget(self.grandPa.housePage)