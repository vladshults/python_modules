#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 10 06 2016

@author: Whesley J Chun
'''

#!/usr/bin/env python
23
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in xrange(randrange(5, 11)):
    dtint = randrange(maxint) # pick date
    dtstr = ctime(dtint) # date string
    llen = randrange(4, 8) # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13) # domain is longer
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)