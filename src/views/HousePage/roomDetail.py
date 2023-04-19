# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomDetailUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from TextButton import TextButton
from button import CustomIconButton

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(567, 648)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(9, 50, 9, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.roomTitle = TextButton("Rumah Sakit")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roomTitle.setFont(font)
        self.roomTitle.setObjectName("roomTitle")
        self.verticalLayout_3.addWidget(self.roomTitle)
        self.roomCap = TextButton("1100 Watt")
        self.roomCap.setObjectName("roomCap")
        self.verticalLayout_3.addWidget(self.roomCap)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: \'#98ABC8\';\n"
"    width: 12px;\n"
"    margin: 20px 0 20px 0;\n"
"    border-radius: 5px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: \'#a1a1a1\';\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: \'#707070\';\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color:\'#707070\';\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: none;\n"
"    height: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 535, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 500))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addElec = QtWidgets.QPushButton(self.widget_3)
        self.addElec.setMinimumSize(QtCore.QSize(0, 40))
        self.addElec.setStyleSheet("background-color: #D9D9D9;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: \'#000000\';")
        self.addElec.setObjectName("addElec")
        self.verticalLayout.addWidget(self.addElec)
        self.frame = QtWidgets.QFrame(self.widget_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setStyleSheet("background-color: #D9D9D9;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: \'#000000\';\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: #D9D9D9;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"color: \'#000000\';\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roomTitle.setText(_translate("Form", "Ruang Tidur"))
        self.roomCap.setText(_translate("Form", "1100 watt"))
        self.addElec.setText(_translate("Form", "tambah"))
        self.pushButton.setText(_translate("Form", "Rice Cooker"))
        self.pushButton_2.setText(_translate("Form", "d"))
        self.pushButton_3.setText(_translate("Form", "Lampu"))
        self.pushButton_4.setText(_translate("Form", "d"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
