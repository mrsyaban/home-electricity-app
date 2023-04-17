from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

class ConsumeLabel(QWidget):
    def __init__(self, consume: int, idHouse: str, mode: bool):
        super().__init__()
        self.idHouse: str = idHouse
        self.mode: bool = mode
        self.consume: int = consume
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Konsumsi Listrik")
        self.value = QLabel(str(self.consume))
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.value)
        self.setLayout(self.layout)

    def handleClick(self):
        print("ebv")
