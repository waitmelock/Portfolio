#-*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from controller import Main 

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())