from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

class PowHouseLabel(QWidget):
    def __init__(self, power: int, idHouse: str, mode: bool):
        super().__init__()
        self.idHouse: str = idHouse
        self.mode: bool = mode
        self.power: int = power
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.layoutLabel  = QVBoxLayout()
        self.label = QLabel("Kapasitas daya")
        self.value = QLabel(str(self.power))
        self.widgetLabel = QWidget()

        self.layoutLabel.addWidget(self.label)
        self.layoutLabel.addWidget(self.value)

        self.widgetLabel.setLayout(self.layoutLabel)
        self.layout.addWidget(self.widgetLabel)

        self.setLayout(self.layout)
