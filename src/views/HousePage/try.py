import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox


class SwitchToggle(QCheckBox):
    stateChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(SwitchToggle, self).__init__(parent)
        self.setFixedSize(60, 34)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255, 255)))
        painter.drawRoundedRect(2, 2, 56, 30, 15, 15)

        if self.isChecked():
            painter.setBrush(QBrush(QColor('#98ABC8')))
            painter.drawRoundedRect(32, 2, 26, 30, 15, 15)
        else:
            painter.setBrush(QBrush(QColor(190, 190, 190, 255)))
            painter.drawRoundedRect(2, 2, 26, 30, 15, 15)

        painter.end()

    def mousePressEvent(self, event):
        self.setChecked(not self.isChecked())
        self.stateChanged.emit(self.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setGeometry(300, 300, 80, 40)

    switch = SwitchToggle(widget)
    switch.move(10, 2)
    switch.stateChanged.connect(lambda state: print(state))

    widget.show()

    sys.exit(app.exec_())
