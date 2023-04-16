from PyQt5.QtWidgets import QPushButton, QStackedWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import QSize

class EditButton(QPushButton):
    def __init__(self, grandPa=None):
        super().__init__()
        self.grandPa: QStackedWidget = grandPa
        self.setStyleSheet('background-color: transparent; border-style: none;')
        icon = QIcon('./././img/Edit.png')
        icon_size = icon.actualSize(QSize(70, 70)) # 100 is the maximum size in pixels
        self.setIcon(icon)
        self.setIconSize(icon_size)
        self.setFixedSize(icon_size)
        self.setIconColor()
    
    def setIconColor(self):
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
        self.grandPa.setCurrentWidget(self.grandPa.mainPage)