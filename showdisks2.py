#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
DifferentExamples.showdisks -- shortdesc

@author:     vlad

@license:    Public Domain

@contact:    vladshulkevich@gmail.com
'''


from abc import ABCMeta, abstractmethod
from platform import system
from sys import argv
from os import remove
import subprocess


class ShowDisks():
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_disks(self):
        pass
    
    @abstractmethod
    def show_partitions(self):
        pass
    

class ShowWinDisks(ShowDisks):
    def __init__(self):
        self.tool = 'diskpart'
        
    def show_disks(self):
        tmp_file = create_tmp_disks()
        self.run_cmd(tmp_file)
        remove(tmp_file)
    
    def show_partitions(self, disk):
        tmp_file = create_tmp_parts()
        self.run_cmd(tmp_file)
        remove(tmp_file)

    def run_cmd(self, tmp_file):
        cmd = self.tool + ' /s %s' % tmp_file
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        out, err = p.communicate()
        exitcode = p.returncode
        if exitcode == 0:
            print out
        else:
            print err
            print out
            print "System error in platform-specific layer! Exit... "
     

class ShowLinDisk(ShowDisks):
    pass


class ShowMacDisks(ShowDisks):
    pass


def platform_detection():
    return system()


def create_tmp_disks():
    tmp_f = 'tmp_file.txt'
    with open(tmp_f, "w") as f:
        s = 'list disk' + '\n'
        f.write(s)
        f.close()
    return tmp_f


def create_tmp_parts():
    tmp_f = 'tmp_file.txt'
    with open(tmp_f, "w") as f:
        s1 = 'select disk %s\n' % str(argv[1])
        s2 = 'list partition\n'
        f.writelines([s1, s2])
        f.close()
    return tmp_f


def usage():
    print "Usage:"
    print "Run \"python showdisks.py\" without arguments shows system disks"
    print "Run \"python showdisks.py n\" with only one numeric argument shows partitions of selected disks"
    print "Run \"python showdisks.py\" with more than one argument \n shows this message and exit"
    print "Run \"python showdisks.py n\" with not-applicable for this system disk number \n prints Error from system layer"


def main():
    if platform_detection() != 'Windows':
        print "Showing disk and partitions of non-windows systems is not implemented yet...\n"
        exit
        
    if platform_detection() == 'Windows':
        d = ShowWinDisks()
        if len(argv) == 1:
            d.show_disks()
        if len(argv) == 2:
            d.show_partitions(argv[1])
        if len(argv) > 2:
            usage()
    
        
if __name__ == '__main__':
    main()
