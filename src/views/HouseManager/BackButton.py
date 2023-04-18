from PyQt5.QtWidgets import QPushButton, QStackedWidget, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import QSize

class BackButton(QPushButton):
    def __init__(self, grandPa2: QStackedWidget, parent=None):
        super().__init__(parent)
        self.grandPa2: QStackedWidget = grandPa2
        self.initUI()

    def initUI(self):
        # self.setText("Kembali")

        self.setStyleSheet("background-color:'#444444; border-style: none;")
        # icon = QIcon('Back.png')
        # icon_size = icon.actualSize(QSize(100, 100)) # 70 is the maximum size in pixels
        # self.setIcon(icon)
        # self.setIconSize(icon_size)
        # self.setFixedSize(icon_size)
        # self.setIconColor()
        
        self.clicked.connect(self.handleClick)
    
    def setIconColor(self) :
        icon = self.icon()
        if icon:
            size = icon.availableSizes()[0]
            pixmap = icon.pixmap(size)
            painter = QPainter(pixmap)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.fillRect(pixmap.rect(), QColor("#444444"))
            painter.end()
            self.setIcon(QIcon(pixmap))

    def handleClick(self):
        self.grandPa2.back()