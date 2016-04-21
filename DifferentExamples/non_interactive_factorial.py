#!/usr/bin/env python -V
# -*- coding: UTF-8 -*-

'''
Created on 30 11 2015
@author: vlad
Function fact() takes a positive integer without any verification of type.
It returns factorial or error.

'''


def fact(n):
    
    if n < 0:
        return False
    
    # According to Factorial definition:
    if n == 1 or n == 0:
        return 1
        
    else:
        cnt = 0
        res = 1
        while cnt < n:
            cnt = cnt + 1
            res = res * cnt 
        return res
    

p = [5, -1, 3, 0, 6]

 
if __name__ == '__main__':
    for i in p:
        print fact(i)
        