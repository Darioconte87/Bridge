'''
Created on 21 lug 2015

@author: DarioConte
'''
from SocketTCP import *
from InterfaceUtils import *

class AIF(object):
    
    def __init__(self):
        pass

Cdb=InterfaceUtils()
AifAddress=Cdb.GetAddress("AIF")
AifIP=AifAddress[0]
AifPort=AifAddress[1]

print("AIF attivo. Porta di ascolto: %d"%AifPort)              
EchoServer(AifIP, AifPort)
asyncore.loop()