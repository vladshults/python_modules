#!/usr/bin/env python -V
# -*- coding: UTF-8 -*-

'''
Created on 21 апр. 2016 г.

@author: vlad
'''

def compareCycledStrings(s1, s2):
    
    res = False
    
    if s1.__len__() != s2.__len__():
        return False
    
    for i in range(0, s1.__len__()):
        cs = s1[i: s1.__len__()] + s1[0: i]
        if cs == s2:
            res = True
    
    return res
    
    
    
    
    
st1 = 'ABCDFF'
st2 = 'CDEFAB'


if __name__ == "__main__":
    if compareCycledStrings(st1, st2) == False:
        print 'String %s is not a result of cycling simbols of string %s' % (st2, st1)
    else:
        print 'String %s is a result of cycling simbols of string %s' % (st2, st1)
