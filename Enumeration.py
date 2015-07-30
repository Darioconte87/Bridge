'''
Created on 30 lug 2015

@author: DarioConte
'''

class Enumeration(object):

    def __init__(self, names):
        for number, name in enumerate(names.split()):
                setattr(self, name, number)
  
'''
#uso di enumeration
foo = Enumeration("bar baz quux")
print(foo.bar)        
'''