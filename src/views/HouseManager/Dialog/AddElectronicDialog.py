from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator

class AddElectronicDialog(QDialog):
    def __init__(self, idRoom):
        super().__init__()
        self.idRoom = idRoom
        self.setWindowTitle("Add Electronic")
        self.setObjectName("Dialog")
        self.resize(500, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(500, 450))
        self.setMaximumSize(QtCore.QSize(500, 450))
        self.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
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
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
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
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignBottom)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(60, -1, 60, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
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
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
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
        self.pushButton.clicked.connect(self.handle_submit)
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi(self)

    def handle_submit(self):
        nama = self.lineEdit.text()
        daya = float(self.lineEdit_2.text())
        voltase = float(self.lineEdit_3.text())
        waktu = float(self.lineEdit_3.text())


        self.accept()
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tambahkan Perangkat Listrik"))
        self.label_2.setText(_translate("Dialog", "Nama Perangkat Listrik"))
        self.label_3.setText(_translate("Dialog", "Daya Perangkat Listrik (Watt)"))
        self.label_4.setText(_translate("Dialog", "Voltase Perangkat Listrik (Volt)"))
        self.label_5.setText(_translate("Dialog", "Waktu Pemakaian per hari (Jam)"))
        self.pushButton.setText(_translate("Dialog", "Tambahkan"))
