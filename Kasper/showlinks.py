#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
DifferentExamples.showlinks -- shortdesc

It is implementation with MetaClass of some bash functionality:
showlinks.py -c is equivalent of "ls -laR /dev | grep lrwxrwxrwx | wc -l"
showlinks.py -l is equivalent of "ls -laR /dev | grep lrwxrwxrwx"

Requarement - wrapper for command "ls -laR /dev"

@author:     vlad

@license:    Public Domain

@contact:    vladshulkevich@gmail.com
'''


from abc import ABCMeta, abstractmethod
from platform import system
from sys import argv
import subprocess


class ShowLinks():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_sl_count(self):
        pass
    
    @abstractmethod
    def get_sl_data(self):
        pass
    

class ShowLinLinks(ShowLinks):
    def __init__(self):
        #self.tool = 'ls -laR /dev'
        pass
        
    def get_sl_count(self):
        ob = self.get_obj_to_parse()
        c = 0
        for line in ob:
    	    if CompareStringWithReg(line) >= 0:
    		c += 1
        return c
        #print "There are %s simlinks in /dev directory." % c
        #print "=====" * 8
        #print ""
        
    def get_sl_data(self):
        ob = self.get_obj_to_parse()
    	li = []
    	for line in ob:
    	    if CompareStringWithReg(line) >= 0:
		li.append(line)
	return li
	
    def run_cmd(self):
        #cmd = self.tool
        p = subprocess.Popen("ls -laR /dev", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        out, err = p.communicate()
        exitcode = p.returncode
        if exitcode == 0:
            return out
        else:
            return err
            exit
            
    def get_obj_to_parse(self):
        s = self.run_cmd()
        return s.split('\n')
        
        
class ShowWinLinks(ShowLinks):
    pass


class ShowMacLinks(ShowLinks):
    pass


def CompareStringWithReg(s):
    return s.find('lrwxrwxrwx')



def platform_detection():
    return system()


def usage():
    print ""
    print "Usage:"
    print "Runing \"python showlinks.py\" without arguments shows amount of simlinks in /dev and info for every link"
    print "Runing \"python showlinks.py n\" with only one argument \"-c\"shows amount of simlinks in /dev"
    print "Runing \"python showlinks.py n\" with only one argument \"-l\"shows info for every simlink in /dev"
    print "" #"Run \"python showdisks.py n\" with more than one argument or with not applicable arguments shows this message"


def main():
    if platform_detection() != 'Linux':
        print "Showing divices simlinks of non-linux systems is not implemented yet...\n"
        exit
        
    if platform_detection() == 'Linux':
        d = ShowLinLinks()
        if len(argv) == 1:
    	    print ""
    	    print "There are %s symlinks in /dev directory" % d.get_sl_count()
    	    print "====="*8
    	    print ""
    	    for i in d.get_sl_data():
    		    print i
    	    usage()
    	    exit
        
        if len(argv) == 2 and argv[1] == '-c':
            print "There are %s symlinks in /dev directory" % d.get_sl_count()
    	    print "====="*8
    	    print ""
            exit
            
        if len(argv) == 2 and argv[1] == '-l':
            for i in d.get_sl_data():
    		    print i
            exit


if __name__ == '__main__':
    main()
