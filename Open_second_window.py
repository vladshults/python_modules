# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys



 
 
class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent, QtCore.Qt.Window)
        self.secondWin = None
        self.build()
 
    def build(self):
        self.mainLayout = QtGui.QVBoxLayout()
 
        self.lab = QtGui.QLabel('simple text', self)
        self.mainLayout.addWidget(self.lab)
 
        self.but1 = QtGui.QPushButton('open window', self)
        self.but1.clicked.connect(self.openWin)
        self.mainLayout.addWidget(self.but1)
 
        self.setLayout(self.mainLayout)
 
    def openWin(self):
        if not self.secondWin:
            self.secondWin = SecondWindow(self)
        self.secondWin.show()
 
 
class SecondWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent, QtCore.Qt.Window)
        self.build()
 
    def build(self):
        self.mainLayout = QtGui.QVBoxLayout()
 
        self.buttons = []
        for i in range(5):
            but = QtGui.QPushButton('button {}'.format(i), self)
            self.mainLayout.addWidget(but)
            self.buttons.append(but)
 
        self.setLayout(self.mainLayout)
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

