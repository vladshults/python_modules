#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 1 06 2016

@author: vladshults

Requirements: - find some percentils for discrete sampling
              - get count and weight of transactions according to time execution
              - get some quantiles from values
              
Base hypothesis: Check of distribution law is a task for numpy or scipy modules.

'''

import re
import numpy
#import scipy.stats as st


fil = 'mtesrl_20150626_MD0000600002_stats.txt'
event = 'ORDER'


def get_arr(input_file):
    print "Parsing data, it may take a long time..."
    li = []
    with open(input_file, 'r') as obj_to_parse:
        for line in obj_to_parse:
            l = re.sub(r'\s+', ' ', line).split(' ')
            if l[1] == event:
                li.append(int(l[6]))
    return li


def get_stats(arr):
    statlist = []
    print "Calculating median, it may take some time..."
    med = numpy.median(arr)
    statlist.append(med)
    print "Calculating min, it may take some time..."
    mini = min(arr)
    statlist.append(mini)
    print "Calculating 90 percentile, it may take some time..."
    p90 = numpy.percentile(arr, 90)
    statlist.append(p90)
    print "Calculating 99 percentile, it may take some time..."
    p99 = numpy.percentile(arr, 99)
    statlist.append(p99)
    print "Calculating 99.9 percentile, it may take some time..."
    p999 = numpy.percentile(arr, 99.9)
    statlist.append(p999)
    return statlist



def create_table_steps(mini, p999, step):
    ste = []
    for z in range((int(mini+5)/5)*5, int(p999), step):
        ste.append(z)
    return ste


def persent_fall(n, ar):
    print st.percentileofscore(ar, n)

def create_table_data(stepp, arr):
    tup_list = []
    le = arr.__len__()
    for i in stepp:
        tup = []
        cnt = 0
        for num in arr:
            if i-5 < num <= i:
                cnt += 1
            tup.append(i)
            tup.append(cnt)
            tup.append(cnt/le)
            tup.append(persent_fall(num, arr))
        tup_list.append(tup)
    return tup_list


if __name__ == '__main__':
    l = get_arr(fil)
    s = get_stats(l)
    steps = create_table_steps(s[1], s[4], 5)
    print create_table_data(steps, l)
    
    print "Median %s" % s[0]
    print "Min %s" % s[1]
    print "p90 %s" % s[2]
    print "p99 %s" % s[3]
    print "p999 %s" % s[4]

