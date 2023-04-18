from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel, QHBoxLayout
from HousePage.BackButton import BackButton

class HousePage(QWidget):
    def __init__(self, parent: QStackedWidget, idHouse: str):
        super().__init__()
        self.id: str = idHouse
        self.parent: QStackedWidget = parent
        self.isSimulate: bool = False 
        self.initUI()

    def initUI(self):
        self.layout: QHBoxLayout = QHBoxLayout()
        self.title: QLabel = QLabel("Detail Rumah " + str(self.id)) 
        self.backButton: BackButton = BackButton(self.parent)

        self.backButton.clicked.connect(self.backButton.handleClick)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.backButton)
        self.setLayout(self.layout)

