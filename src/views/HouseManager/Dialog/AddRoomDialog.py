from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from models.Room import *

class AddRoomDialog(QDialog):
    def __init__(self, idHouse, grandPa1):
        self.idHouse = idHouse
        self.grandPa1 = grandPa1
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(500, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(500, 250))
        self.setMaximumSize(QSize(500, 250))
        self.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QFrame(self)
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignBottom)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #939393;\n"
"    border-radius: 13px;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #444444;\n"
"}")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QFrame(self)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignBottom)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: #939393;\n"
"    border-radius: 13px;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #444444;\n"
"}")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QDoubleValidator(0, 10000, 0, self))
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)
        self.frame_2 = QFrame(self)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.clicked.connect(self.handle_submit)
        font = QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #444444;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: rgb(217, 217, 217);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Nama Ruangan"))
        self.label_3.setText(_translate("Dialog", "Kapasitas Daya (Watt)"))
        self.pushButton.setText(_translate("Dialog", "Tambahkan"))

    def handle_submit(self):
        name = self.lineEdit.text()
        power = int(self.lineEdit_2.text())
        x = Room(name, self.idHouse, power)
        self.grandPa1.reload()
        self.accept()
