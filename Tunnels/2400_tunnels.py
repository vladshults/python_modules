#!/usr/bin/env python -V
# -*- coding: UTF-8 -*-

'''
Created on 28 ���. 2016 �.
@author: vlad
'''

obj_list = []
ip_tun_list = []
conn_number_list = []
id_list = []
counter = 0
single_ip = '172.16.0.1'
src_network_list = []
cn_serial = '4150'
local_cn = '2'
remote_cn = '1'

start_netw = '172.16.'
start_src_netw = '10.10.'
netw_range = range(1, 11)
ip_range = range(0, 256)

for i in netw_range:
    for z in ip_range:
        adr = start_netw + str(i) + '.' + str(z)
        src_adr = start_src_netw + str(i) + '.' + str(z)
        ip_tun_list.append(adr)
        src_network_list.append(src_adr)


for ip in ip_tun_list:
    print ' ip secondary-address ' + ip + '/16'

#print ''

for y in ip_tun_list:
    counter = counter + 1
    c_id = str(counter + 10000)
    conn_id = 't' + c_id
    #print ''
    print 'crypto disec conn ' + conn_id
    print ' alg encryption'
    print ' id ' + str(c_id)
    print ' local ip ' + y
    print ' remote ip ' + single_ip
    print ' serial 4150'
    print ' local cn 2'
    print ' remote cn 1'
    print ' permit src ' + src_network_list[counter - 1] + '/32 ' + 'dst 10.100.0.0/24'
    print ''
    print 'crypto disec enable conn ' + conn_id
    print ''
    pass

print ' ################################################################################'
print ' ################################################################################'
print ' ################################################################################'

print ''

counter = 0
for y in ip_tun_list:
    counter = counter + 1
    c_id = str(counter + 10000)
    conn_id = 't' + c_id
    #print ''
    print 'crypto disec conn ' + conn_id
    print ' alg encryption'
    print ' id ' + str(c_id)
    print ' local ip ' + single_ip
    print ' remote ip ' + y
    print ' serial 4150'
    print ' local cn 1'
    print ' remote cn 2'
    print ' permit src 10.100.0.0/24 ' + 'dst ' + src_network_list[counter - 1] + '/32 ' 
    print ''
    print 'crypto disec enable conn ' + conn_id
    print ''
    pass

if __name__ == '__main__':
    pass
