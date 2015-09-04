'''
Created on 21 lug 2015

@author: DarioConte
'''
from SocketTCP import *

class AIF(object):
    
    def __init__(self):
        pass
    
print("AIF attivo. Porta di ascolto: 15000")              
EchoServer('localhost', 15000)
asyncore.loop()