'''
Created on 21 lug 2015

@author: DarioConte
'''
from TCPAcgInterface import *
from ClientTCP import *
from AIF import *

if __name__ == '__main__':
    
    print("Avvio del Bridge")
    
    Terminale=TCPAcgInterface()
    Terminale.m_Run()
    
    ACGr=ClientTCP()
    ACGr.OpenClient("127.0.0.1", 15000)
    ACGr.Send("HOLAAAAAAAAAA")
    '''
    aif=AIF()
    aif.OpenServer("127.0.0.1", 15001) 
    '''