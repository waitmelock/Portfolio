# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q1234_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Q3 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q3.setGeometry(QtCore.QRect(510, 20, 150, 275))
        self.Q3.setObjectName("Q3")
        self.Button_3_1 = QtWidgets.QPushButton(self.Q3)
        self.Button_3_1.setGeometry(QtCore.QRect(20, 130, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3_1.sizePolicy().hasHeightForWidth())
        self.Button_3_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_3_1.setFont(font)
        self.Button_3_1.setAutoDefault(False)
        self.Button_3_1.setDefault(False)
        self.Button_3_1.setObjectName("Button_3_1")
        self.Button_3_2 = QtWidgets.QPushButton(self.Q3)
        self.Button_3_2.setGeometry(QtCore.QRect(20, 200, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3_2.sizePolicy().hasHeightForWidth())
        self.Button_3_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_3_2.setFont(font)
        self.Button_3_2.setAutoDefault(False)
        self.Button_3_2.setDefault(False)
        self.Button_3_2.setObjectName("Button_3_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Q3)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 55, 110, 25))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Q2 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q2.setGeometry(QtCore.QRect(350, 20, 150, 275))
        self.Q2.setObjectName("Q2")
        self.Button_2_1 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_1.setGeometry(QtCore.QRect(20, 30, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_1.sizePolicy().hasHeightForWidth())
        self.Button_2_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_1.setFont(font)
        self.Button_2_1.setAutoDefault(False)
        self.Button_2_1.setDefault(False)
        self.Button_2_1.setObjectName("Button_2_1")
        self.Button_2_2 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_2.setGeometry(QtCore.QRect(20, 70, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_2.sizePolicy().hasHeightForWidth())
        self.Button_2_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_2.setFont(font)
        self.Button_2_2.setAutoDefault(False)
        self.Button_2_2.setDefault(False)
        self.Button_2_2.setObjectName("Button_2_2")
        self.Q2_3 = QtWidgets.QGroupBox(self.Q2)
        self.Q2_3.setGeometry(QtCore.QRect(10, 110, 130, 71))
        self.Q2_3.setObjectName("Q2_3")
        self.Button_2_3 = QtWidgets.QPushButton(self.Q2_3)
        self.Button_2_3.setGeometry(QtCore.QRect(10, 40, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_3.sizePolicy().hasHeightForWidth())
        self.Button_2_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_3.setFont(font)
        self.Button_2_3.setAutoDefault(False)
        self.Button_2_3.setDefault(False)
        self.Button_2_3.setObjectName("Button_2_3")
        self.label_2_3 = QtWidgets.QLabel(self.Q2_3)
        self.label_2_3.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.label_2_3.setObjectName("label_2_3")
        self.spinBox2_3 = QtWidgets.QSpinBox(self.Q2_3)
        self.spinBox2_3.setGeometry(QtCore.QRect(62, 11, 50, 22))
        self.spinBox2_3.setReadOnly(False)
        self.spinBox2_3.setMinimum(1)
        self.spinBox2_3.setMaximum(15)
        self.spinBox2_3.setObjectName("spinBox2_3")
        self.Button_2_4 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_4.setGeometry(QtCore.QRect(20, 190, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_4.sizePolicy().hasHeightForWidth())
        self.Button_2_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_4.setFont(font)
        self.Button_2_4.setAutoDefault(False)
        self.Button_2_4.setDefault(False)
        self.Button_2_4.setObjectName("Button_2_4")
        self.Button_2_5 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_5.setGeometry(QtCore.QRect(20, 230, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_5.sizePolicy().hasHeightForWidth())
        self.Button_2_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_5.setFont(font)
        self.Button_2_5.setAutoDefault(False)
        self.Button_2_5.setDefault(False)
        self.Button_2_5.setObjectName("Button_2_5")
        self.Q4 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q4.setGeometry(QtCore.QRect(670, 20, 150, 275))
        self.Q4.setObjectName("Q4")
        self.Button_4_1 = QtWidgets.QPushButton(self.Q4)
        self.Button_4_1.setGeometry(QtCore.QRect(20, 130, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4_1.sizePolicy().hasHeightForWidth())
        self.Button_4_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_4_1.setFont(font)
        self.Button_4_1.setAutoDefault(False)
        self.Button_4_1.setDefault(False)
        self.Button_4_1.setObjectName("Button_4_1")
        self.LoadButton = QtWidgets.QGroupBox(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(30, 20, 150, 275))
        self.LoadButton.setObjectName("LoadButton")
        self.Button_Folder = QtWidgets.QPushButton(self.LoadButton)
        self.Button_Folder.setGeometry(QtCore.QRect(20, 60, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Folder.sizePolicy().hasHeightForWidth())
        self.Button_Folder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_Folder.setFont(font)
        self.Button_Folder.setAutoDefault(False)
        self.Button_Folder.setDefault(False)
        self.Button_Folder.setObjectName("Button_Folder")
        self.Button_LoadL = QtWidgets.QPushButton(self.LoadButton)
        self.Button_LoadL.setGeometry(QtCore.QRect(20, 120, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_LoadL.sizePolicy().hasHeightForWidth())
        self.Button_LoadL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_LoadL.setFont(font)
        self.Button_LoadL.setAutoDefault(False)
        self.Button_LoadL.setDefault(False)
        self.Button_LoadL.setObjectName("Button_LoadL")
        self.Button_LoadR = QtWidgets.QPushButton(self.LoadButton)
        self.Button_LoadR.setGeometry(QtCore.QRect(20, 180, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_LoadR.sizePolicy().hasHeightForWidth())
        self.Button_LoadR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_LoadR.setFont(font)
        self.Button_LoadR.setAutoDefault(False)
        self.Button_LoadR.setDefault(False)
        self.Button_LoadR.setObjectName("Button_LoadR")
        self.Q1 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q1.setGeometry(QtCore.QRect(190, 20, 150, 275))
        self.Q1.setObjectName("Q1")
        self.Button_1_1 = QtWidgets.QPushButton(self.Q1)
        self.Button_1_1.setGeometry(QtCore.QRect(20, 90, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1_1.sizePolicy().hasHeightForWidth())
        self.Button_1_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_1_1.setFont(font)
        self.Button_1_1.setAutoDefault(False)
        self.Button_1_1.setDefault(False)
        self.Button_1_1.setObjectName("Button_1_1")
        self.Button_1_2 = QtWidgets.QPushButton(self.Q1)
        self.Button_1_2.setGeometry(QtCore.QRect(20, 150, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1_2.sizePolicy().hasHeightForWidth())
        self.Button_1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_1_2.setFont(font)
        self.Button_1_2.setAutoDefault(False)
        self.Button_1_2.setDefault(False)
        self.Button_1_2.setObjectName("Button_1_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2021 OpenCV Hw1"))
        self.Q3.setTitle(_translate("MainWindow", "3. Augmented Reality"))
        self.Button_3_1.setText(_translate("MainWindow", "3.1 Sow Words on Board"))
        self.Button_3_2.setText(_translate("MainWindow", "3.2 Sow Words Vertically"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.Q2.setTitle(_translate("MainWindow", "2. Calibration"))
        self.Button_2_1.setText(_translate("MainWindow", "2.1 Find Corners "))
        self.Button_2_2.setText(_translate("MainWindow", "2.2 Find Intrinsic"))
        self.Q2_3.setTitle(_translate("MainWindow", "2.3"))
        self.Button_2_3.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.label_2_3.setText(_translate("MainWindow", "Select image:"))
        self.Button_2_4.setText(_translate("MainWindow", "2.4 Find Distortion"))
        self.Button_2_5.setText(_translate("MainWindow", "2.5 Show Result"))
        self.Q4.setTitle(_translate("MainWindow", "4. Stereo Disparity Map "))
        self.Button_4_1.setText(_translate("MainWindow", "4.1 Stereo Disparity Map"))
        self.LoadButton.setTitle(_translate("MainWindow", "Load Data"))
        self.Button_Folder.setText(_translate("MainWindow", "Load Folder"))
        self.Button_LoadL.setText(_translate("MainWindow", "Load Image_L"))
        self.Button_LoadR.setText(_translate("MainWindow", "Load Image_R"))
        self.Q1.setTitle(_translate("MainWindow", "1. Find contour"))
        self.Button_1_1.setText(_translate("MainWindow", "1.1 Draw Contour"))
        self.Button_1_2.setText(_translate("MainWindow", "1.2 Count Rings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
