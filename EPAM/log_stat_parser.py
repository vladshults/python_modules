#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Created on 04 06 2016

@author: vladshults

Requirements: - find some percentils for discrete sampling
              - get count and weight of transactions according to time execution
              - get some quantiles from values
              
Base hypothesis: Check of distribution law is a task for numpy or scipy module.
"""

import re
import numpy as np


fil = 'mtesrl_20150626_MD0000600002_stats.txt'
event = 'ORDER'


def get_arr(input_file):
    print "Parsing data, it may take a long time..."
    li = []
    with open(input_file, 'r') as obj_to_parse:
        for line in obj_to_parse:
            ln = re.sub(r'\s+', ' ', line).split(' ')
            if ln[1] == event:
                li.append(int(ln[6]))
    return li


def get_stats(arr):
    statlist = []
    print "Calculating median, it may take some time..."
    med = np.median(arr)
    statlist.append(int(med))
    print "Calculating min, it may take some time..."
    mini = min(arr)
    statlist.append(int(mini))
    print "Calculating 90 percentile, it may take some time..."
    p90 = np.percentile(arr, 90)
    statlist.append(int(p90))
    print "Calculating 99 percentile, it may take some time..."
    p99 = np.percentile(arr, 99)
    statlist.append(int(p99))
    print "Calculating 99.9 percentile, it may take some time..."
    p999 = np.percentile(arr, 99.9)
    statlist.append(int(p999))
    return statlist


def create_table_steps(mini, p999, step):
    ste = []
    for z in range((int(mini+step)/step)*step, int(p999)+step, step):
        ste.append(z)
    return ste

'''
def persent_ofall(ar, n, step):
    return st.percentileofscore(ar, n, kind='weak')
'''


def trans_no(ar, n, step):
    cnt = 0
    sm = 0
    for num in ar:
        if n-step < num <= n:
            cnt += 1
        if num <= n:
            sm += 1
    return cnt, sm


def create_table_data(arr, stepp):
    print "Calculating data for every step, it may take a long time..."
    dat = []
    leng = arr.__len__()
    for stp in stepp:
        dataset = []
        t = trans_no(arr, stp, (stepp[1] - stepp[0]))
        t_n = t[0]
        t_w = t[1]
        weight = round((t_n/float(leng)*100.0), 2)
        percs = round((t_w/float(leng)*100.0), 2)
        dataset.append(stp)
        dataset.append(t_n)
        dataset.append(weight)
        dataset.append(percs)
        dat.append(dataset)
    return dat


def print_stats(sts):
    print ""
    print 'Common statistics for event: %s' % event
    print 'Min={0}, Median={1}, 90%={2}, 99%={3}, 99.9%={4}'.format(sts[1], sts[0], sts[2], sts[3], sts[4])


def print_table(data):
    print ""
    print 'Ex_Time Trans_No Weght,% Percent'
    print '================================'
    for item in data:
        print('{0:4} {1:8} {2:8} {3:8}'.format(item[0], item[1], item[2], item[3]))
    print '================================'


if __name__ == '__main__':
    l = get_arr(fil)
    s = get_stats(l)
    steps = create_table_steps(s[1], s[4], 5)
    d = create_table_data(l, steps)
    print_table(d)
    print_stats(s)
