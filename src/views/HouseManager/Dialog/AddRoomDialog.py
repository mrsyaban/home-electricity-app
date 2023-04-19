from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from controller.roomController import *

class AddRoomDialog(QDialog):
    def __init__(self, idHouse, grandPa1):
        super().__init__()
        self.idHouse = idHouse
        self.grandpa2 = grandPa1
        self.setWindowTitle("My Dialog")

        layout = QVBoxLayout(self)

        label1 = QLabel("Enter room name:")
        self.input1 = QLineEdit()

        label2 = QLabel("Enter power:")
        self.input2 = QSpinBox()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.handle_submit)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.reject)

        layout.addWidget(label1)
        layout.addWidget(self.input1)
        layout.addWidget(label2)
        layout.addWidget(self.input2)
        layout.addWidget(submit_button)
        layout.addWidget(close_button)

    def handle_submit(self):
        name = self.input1.text()
        power = self.input2.value()
        x = RoomController.add(name, self.idHouse, power)
        self.grandpa2.reload()
        self.accept()
