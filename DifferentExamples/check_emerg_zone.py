#!/usr/bin/env python -V
# -*- coding: UTF-8 -*-

'''
Created on 30 11 2015
@author: vlad
Function squareTrack() takes a tuple of pairs of values - rotation angle in degrees and 
the distance to the point.
It returns "True" if the point is in the 2x2 square centered at the (0, 0), 
"False" if point is outside the square.

'''

import math

'''' Points inside the incircle do not have to be counted, because they are obviously
inside the square '''
minR = 1
'''' Points outside the circumcircle do not have to be counted, because they are obviously
outside the square '''
maxR = math.sqrt(2)


def squareTrack(tu):
    
    if tu[1] > maxR:
        return False
    
    if 0 <= tu[1] <= minR:
        return True
    
    try:
        if tu[1] < 0 or tu[0] < 0:
            raise SystemError
    except SystemError:
        print ('Unknown System Error!\n')
        return
    
    fi = (((tu[0]+45)%90)-45) * math.pi / 180
    if 1 / math.cos(fi) < tu[1]:
        return False
    else:
        return True


p = [(37, 1.1), (999, 1.6), (20, -1), (-20, 1.8)]

 
if __name__ == '__main__':
    for i in p:
        if squareTrack(i) == True:
            print ('Alarm! Object is in emergency square!\n')
        elif squareTrack(i) == False:
            print ('0\n')
        else:
            pass
