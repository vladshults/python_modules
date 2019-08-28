'''
Created on 6 06 2016
@author: vlad
'''

class SingletonMeta(type):
    def __init__(self, *args, **kw):
        self.instance = None
    def __call__(self, *args, **kw):
        if self.instance is None:
            self.instance = super(SingletonMeta, self).__call__(*args, **kw)
        return self.instance


class C(object):
    __metaclass__ = SingletonMeta


foo = C()
foo.x = 42
bar = C()
print bar.x
