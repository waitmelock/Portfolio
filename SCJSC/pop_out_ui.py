# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_out.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 361, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_activity = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_activity.setFont(font)
        self.comboBox_activity.setObjectName("comboBox_activity")
        self.comboBox_activity.addItem("")
        self.comboBox_activity.addItem("")
        self.comboBox_activity.addItem("")
        self.comboBox_activity.addItem("")
        self.comboBox_activity.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_activity)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_group = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_group.setFont(font)
        self.comboBox_group.setObjectName("comboBox_group")
        self.comboBox_group.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_group)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_budget = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_budget.setFont(font)
        self.label_budget.setObjectName("label_budget")
        self.gridLayout.addWidget(self.label_budget, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_budget_showcondition = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_budget_showcondition.setFont(font)
        self.label_budget_showcondition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_budget_showcondition.setObjectName("label_budget_showcondition")
        self.horizontalLayout_2.addWidget(self.label_budget_showcondition)
        self.pushButton_check = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout_2.addWidget(self.pushButton_check)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_activity.setCurrentText(_translate("Form", "請選擇活動"))
        self.comboBox_activity.setItemText(0, _translate("Form", "請選擇活動"))
        self.comboBox_activity.setItemText(1, _translate("Form", "舞風費"))
        self.comboBox_activity.setItemText(2, _translate("Form", "期初舞展"))
        self.comboBox_activity.setItemText(3, _translate("Form", "小成"))
        self.comboBox_activity.setItemText(4, _translate("Form", "大成"))
        self.comboBox_group.setItemText(0, _translate("Form", "請選擇項目"))
        self.label_budget.setText(_translate("Form", "預算:"))
        self.label_budget_showcondition.setText(_translate("Form", "無輸入內容"))
        self.pushButton_check.setText(_translate("Form", "確認"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

