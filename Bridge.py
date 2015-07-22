'''
Created on 21 lug 2015

@author: DarioConte
'''
from ClientTCP import *
from AIF import *
from TCPInterface import *
from MyThread import *
if __name__ == '__main__':
    
    print("Avvio del Bridge")
    AvvioInterfacciaACG=TCPInterface("ACG")
    AvvioInterfacciaACG.start()
    
    
    '''AvvioInterfacciaACG.stop()
    AvvioInterfacciaACG=TCPInterface("AIF")
    AvvioInterfacciaACG.start()
    '''
    '''
    Terminale=TCPAcgInterface()
    Terminale.m_Run()
    
    ACGr=ClientTCP()
    ACGr.OpenClient("127.0.0.1", 15000)
    ACGr.Send("HOLAAAAAAAAAA")
    
    aif=AIF()
    aif.OpenServer("127.0.0.1", 15001) 
    '''