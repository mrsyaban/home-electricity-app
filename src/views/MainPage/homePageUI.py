from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from houseListButton import HouseButton
from addButton import AddButton

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1109, 614)
        self.page = QtWidgets.QWidget()
        self.page.setMinimumSize(QtCore.QSize(768, 432))
        self.page.setMaximumSize(QtCore.QSize(1536, 864))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setObjectName("logo")
        # Load the image from file
        pixmap = QtGui.QPixmap("./././img/logo.png").scaled(300, 200)

        # Set the pixmap as the label's background
        self.logo.setPixmap(pixmap)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)


        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.frame1 = QtWidgets.QFrame(self.frame_2)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setContentsMargins(250, -1, 250, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.plusButton = AddButton('./././img/plus.png')
        self.plusButton.setObjectName("plusButton")
        self.horizontalLayout_2.addWidget(self.plusButton)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame1)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = HouseButton("Rumah Angker", "./././img/right.png")

        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = HouseButton("Rumah Mantan", "./././img/right.png")

        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame1)
        self.verticalLayout.addWidget(self.frame_2)
        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        # self.logo.setText(_translate("StackedWidget", "Logo"))
        self.label.setText(_translate("StackedWidget", "Daftar Tabel"))
        # self.plusButton.setText(_translate("StackedWidget", "plus"))
        # self.pushButton.setText(_translate("StackedWidget", "Rumah Angker"))
        # self.pushButton_2.setText(_translate("StackedWidget", "Rumah Mantan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
