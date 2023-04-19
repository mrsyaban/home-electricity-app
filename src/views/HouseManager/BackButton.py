from PyQt5.QtWidgets import QPushButton, QStackedWidget, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import QSize
from utils.getDirPath import *

class BackButton(QPushButton):
    def __init__(self, grandPa2: QStackedWidget, parent=None):
        super().__init__(parent)
        self.grandPa2: QStackedWidget = grandPa2
        self.initUI()

    def initUI(self):
        self.clicked.connect(self.handleClick) 
        self.setStyleSheet('QPushButton { background-color: transparent; border-radius: 7px;} QPushButton::hover  { background-color: #999999;}')
        icon = QIcon(f'{getDirPath()}/src/assets/Back.png')
        icon_size = icon.actualSize(QSize(100, 100)) # 70 is the maximum size in pixels
        self.setIcon(icon)
        self.setIconSize(icon_size)
        self.setFixedSize(icon_size)

    def handleClick(self):
        self.grandPa2.back()