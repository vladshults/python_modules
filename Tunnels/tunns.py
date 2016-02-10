# -*- coding: UTF-8 -*-

'''
Created on 2 ����. 2016 �.

@author: vlad
'''

import sys
from PyQt4 import QtGui, QtCore
from Example_1 import MyWindow

   
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(650, 450)
        self.setWindowTitle('Tunnels for NX conf generator')

        MWidget = QtGui.QDesktopWidget()
        #MWidget.add()
        self.setCentralWidget(MWidget)
         
        ex = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        ex.setShortcut('Ctrl+Q')
        ex.setStatusTip('Exit application')
        self.connect(ex, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        ge = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Generate many to one', self)
        ge.setShortcut('Ctrl+G')
        ge.setStatusTip('Generate tunnels')
        self.connect(ge, QtCore.SIGNAL('triggered()'), self.call_ge_window)
        
        gem = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Generate many to many', self)
        gem.setShortcut('Ctrl+M')
        gem.setStatusTip('Generate another style of tunnels')
        self.connect(gem, QtCore.SIGNAL('triggered()'), self.call_gem_window)
        
        menubar = self.menuBar()
        
        fi = menubar.addMenu('&File')
        fi.addAction(ge)
        fi.addAction(gem)
        fi.addAction(ex)
        
    def call_gem_window(self):
        self.window = MyWindow() # Создаем экземпляр класса
        self.window.setWindowTitle("OOP style of window creation")
        self.window.resize(350, 150)
        self.window.show()
    
    def call_ge_window(self):
        self.window = MyWindow() # Создаем экземпляр класса
        self.window.setWindowTitle("OOP style of window creation - tunnels of first type")
        self.window.resize(650, 150)
        self.window.show()
    
        

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
