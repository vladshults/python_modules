#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 24 ��� 2016 �.

@author: vlad
'''


def multiple_of_3(number):
    return number % 3 == 0

def multiple_of_5(number):
    return number % 5 == 0
    
for i in range(1, 100):
    if not multiple_of_3(i) and not multiple_of_5(i):
        print i
        continue
    
    if multiple_of_3(i) and multiple_of_5(i):
        print "fizzbuzz"
        continue
        
    else:
        print ["fizz", "buzz"][multiple_of_5(i)]
     
