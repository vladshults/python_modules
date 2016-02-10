# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class ComboBoxBasic(QtGui.QWidget):
    def __init__(self):
        # create variables
        self.param_list = []
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('NX tunnels generator: Choose amount of tunnels')
        self.resize(350,80)
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        self.combo = QtGui.QComboBox()
        self.vbox.addWidget(self.combo)
        self.lbl = QtGui.QLabel('10')
        self.lbl1 = QtGui.QLabel('You have choosen')
        self.lbl.setAlignment(QtCore.Qt.AlignLeft)
        self.but1 = QtGui.QPushButton('GENERATE', self)
        self.but1.clicked.connect(self.generate)
        self.but2 = QtGui.QPushButton('CLOSE', self)
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.but1)
        self.vbox.addWidget(self.but2)
        tunnellist = ['10', '50', '100', '250', '256', '512', '1024', '1536', '2048', '2560', '5120', '10240']
        self.combo.addItems(tunnellist)
        self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
        self.connect(self.but2, QtCore.SIGNAL("clicked()"), QtCore.SLOT("close()"))

    def combo_chosen(self, text):
        self.lbl.setText(text)
        index = self.combo.currentIndex()
        if index == 0:
            self.param_list = TunData().param_list10
        elif index == 1:
            self.param_list = TunData().param_list50
        elif index == 2:
            self.param_list = TunData().param_list100
        elif index == 3:
            self.param_list = TunData().param_list250
        elif index == 4:
            self.param_list = TunData().param_list256
        elif index == 5:
            self.param_list = TunData().param_list512
        elif index == 6:
            self.param_list = TunData().param_list1024
        elif index == 7:
            self.param_list = TunData().param_list1536
        elif index == 8:
            self.param_list = TunData().param_list2048
        elif index == 9:
            self.param_list = TunData().param_list2560
        elif index == 10:
            self.param_list = TunData().param_list5120
        elif index == 11:
            self.param_list = TunData().param_list10240

    def generate(self):
        g = Generate(self.param_list)
        g.generate_ip_lists()
        g.generate_many_to_one()
        

class Generate:
    def __init__(self, param_list):
        self.ip_tun_list = []
        self.ip_receive_tun_list = []
        self.src_network_list = []
        self.param_list = param_list
        self.netw_range = range(param_list[0], param_list[1])
        self.ip_range = range(param_list[2], param_list[3])
        self.single_ip = str(param_list[4]) + '0.1'
        self.single_receive_ip = str(param_list[4]) + '100.1'
        self.src_network = str(param_list[6])
        self.cn_serial = str(param_list[7])
        
    def generate_ip_lists(self):
        for y in self.netw_range:
                for z in self.ip_range:
                    adr = str(self.param_list[4]) + str(y) + '.' + str(z)
                    self.ip_tun_list.append(adr)
                    src_adr = str(self.param_list[5]) + str(y) + '.' + str(z)
                    self.src_network_list.append(src_adr)
                    
    def generate_many_to_one(self):
        with open(r"secondary_ips.txt", "w") as f:
            for ip in self.ip_tun_list:
                s = ' ip secondary-address ' + ip + '/16\n'
                f.write(s)
        f.close()
        
        with open(r"tunnels_from_many_ips.txt", "w") as f:
            counter = 0
            for ip in self.ip_tun_list:
                counter = counter + 1
                c_id = str(counter + 10000)
                conn_id = 't' + c_id
                s1  = 'crypto disec conn ' + conn_id + '\n'
                s2  = ' alg encryption' + '\n'
                s3  = ' id ' + str(c_id) + '\n'
                s4  = ' local ip ' + ip + '\n'
                s5  = ' remote ip ' + self.single_ip + '\n'
                s6  = ' serial 4150' + '\n'
                s7  = ' local cn 2' + '\n'
                s8  = ' remote cn 1' + '\n'
                s9  = ' permit src ' + self.src_network_list[counter - 1] + '/32 ' + 'dst ' + self.src_network + '0.0/24' + '\n'
                s10 = '\n'
                s11 = 'crypto disec enable conn ' + conn_id + '\n'
                s12 = '\n'
                f.writelines([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
        f.close()
        
        with open(r"tunnels_from_single_ip.txt", "w") as f:
            counter = 0
            for ip in self.ip_tun_list:
                counter = counter + 1
                c_id = str(counter + 10000)
                conn_id = 't' + c_id
                s1  = 'crypto disec conn ' + conn_id + '\n'
                s2  = ' alg encryption' + '\n'
                s3  =  ' id ' + str(c_id) + '\n'
                s4  = ' local ip ' + self.single_ip + '\n'
                s5  = ' remote ip ' + ip + '\n'
                s6  = ' serial 4150' + '\n'
                s7  = ' local cn 1' + '\n'
                s8  = ' remote cn 2' + '\n'
                s9  = ' permit src ' + self.src_network + '0.0/24 ' + 'dst ' + self.src_network_list[counter - 1] + '/32 '  + '\n'
                s10 = '\n'
                s11 = 'crypto disec enable conn ' + conn_id + '\n'
                s12 = '\n'
                f.writelines([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
        f.close()        


class TunData:
    def __init__(self):
        self.param_list10    = [ 1, 2, 0, 10, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list50    = [ 1, 2, 0, 50, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list100   = [ 1, 2, 0, 100, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list250   = [ 1, 2, 0, 250, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list256   = [ 1, 2, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list512   = [ 1, 3, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list1024  = [ 1, 5, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list1536  = [ 1, 7, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list2048  = [ 1, 9, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list2560  = [ 1, 11, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list5120  = [ 1, 21, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
        self.param_list10240 = [ 1, 41, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]


def main():
    app = QtGui.QApplication(sys.argv)
    gui = ComboBoxBasic()
    gui.show()
    app.exec_()

if __name__ == "__main__":
        main()
