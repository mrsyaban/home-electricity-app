import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class TextButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet('background-color: transparent; border-style: none;')