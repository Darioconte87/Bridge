'''
Created on 20 lug 2015

@author: DarioConte
'''
from Configuration import *
from TCPSimulatorThread import *
from MyThread import *

class TCPAcgInterface(object):
    
    def __init__(self):
        self.simulatorThread = 0;
    
    def m_Run(self):
        label="ACG"
        #prende il file di configurazione specificato nella classe Configuration
        configuration=Configuration()
        #leggi i parametri dal file di configurazione a seconda della label
        configuration.ReadConfigurationFromFile()
        Object_Label=Configuration.IPAddressMap[label]
        print("Metto in ascolto l'interaccia %s su %s: %s" %(label,Object_Label.IP,Object_Label.Port))
        thread=TCPSimulatorThread(label,Object_Label.IP,Object_Label.Port,Object_Label.Multicast,Object_Label.MessageType,Object_Label.SocketType)
        
        
        
Interfaccia=TCPAcgInterface()
Interfaccia.m_Run()