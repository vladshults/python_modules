#!/usr/bin/env python -V
# -*- coding: UTF-8 -*-


def palindrom(s):
    n = 0
    m = len(s) - 1

    while n <= m:
        sim1 = s[n]
        sim2 = s[m]

        if not sim1.isalpha():
            n += 1
            continue

        if not sim2.isalpha():
            m -= 1
            continue

        if sim1 != sim2:
            return False

        n += 1
        m -= 1

    return True


s1 = 'ABABA---111'
s2 = '___ABA==='
s3 = 'abcde'


if __name__ == '__main__':
    for st in [s1, s2, s3]:
        if palindrom(st):
            print 'String %r is a palindrom' % st
        else:
            print 'String %r is not a palindrom' % st
