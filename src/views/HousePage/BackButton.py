from PyQt5.QtWidgets import QPushButton, QStackedWidget

class BackButton(QPushButton):
    def __init__(self, grandPa: QStackedWidget):
        super().__init__()
        self.grandPa: QStackedWidget = grandPa
        self.initUI()

    def initUI(self):
        self.setText("Kembali")

    def handleClick(self):
        self.grandPa.setCurrentWidget(self.grandPa.mainPage)
