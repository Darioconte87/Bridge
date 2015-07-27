'''
Created on 22 lug 2015

@author: DarioConte
'''

from MyThread import *
from Configuration import *
from TCPSimulatorThread import *

class TCPInterface(MyThread):

    ConfigurationPaths={"ACG":"../BridgeACG.ini","AIF":"../BridgeAIF.ini"}
    
    def __init__(self, label):
        MyThread.__init__(self)
        self.label=label
        self.path=""
        
    def run(self):
        MyThread.run(self)
        self.path=self.ConfigurationPaths[self.label]
        #prende il file di configurazione specificato nella classe Configuration
        configuration=Configuration()
        #leggi i parametri dal file di configurazione a seconda della label
        configuration.ReadConfigurationFromFile(self.path)
        Object_Label=Configuration.IPAddressMap[self.label]
        print("Metto in ascolto l'interaccia %s su %s: %s" %(self.label,Object_Label.IP,Object_Label.Port)) 
        thread=TCPSimulatorThread(self.label,Object_Label.IP,Object_Label.Port,Object_Label.Multicast,Object_Label.MessageType,Object_Label.SocketType)
        thread.start()