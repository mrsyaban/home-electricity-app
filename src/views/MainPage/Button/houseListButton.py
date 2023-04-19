from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class HouseButton(QPushButton):
    def __init__(self, text, icon_file, parent=None):
        super().__init__(parent)
        self.setText(text)
        icon = QIcon(icon_file)
        self.setIcon(icon)
        self.setMinimumSize(QSize(0, 40))
        self.setIconSize(QSize(16, 16))
        # self.setFixedWidth(100)
        self.setStyleSheet( "QPushButton { text-align: left; padding-left: 20px; background-color: #D9D9D9;\n"
                            "font: 75 12pt \"MS Shell Dlg 2\";\n"
                            "border-radius: 20px;\n"
                            "padding: 5px;\n"
                            "padding-left: 15px;\n"
                            "padding-right: 15px;\n"
                            "color: \'#000000\';}\n"
                            "QPushButton::icon {\n"
                            "margin-right: 0px;\n"
                            "margin-left: 50px;}\n"
                            "QPushButton::hover  { background-color: #999999;}\n")

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    button = HouseButton("Rumah Angker", "./././img/right.png", window)
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(button)
    window.show()
    app.exec_()
