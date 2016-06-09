#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 9 06 2016

@author: vlad

'''

import xml.etree.ElementTree as e
from xml.etree.ElementTree import SubElement


tree = e.parse('input.xml')
root = tree.getroot()


def serv_to_custom():
    root[0][0].text = 'Custom'
    SubElement(root[0][1], "item")
    root[0][1][0].text = 'http://kaspersky.com'
    tree.write("input.xml")


def custom_to_serv():
    root[0][0].text = 'KLServers'
    root[0][1].__delitem__(0)
    tree.write("input.xml")


if root[0][0].text == 'KLServers':
    serv_to_custom()
else:
    custom_to_serv()
    
