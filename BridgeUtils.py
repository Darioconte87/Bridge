'''
Created on 11 set 2015

@author: DarioConte
'''

from Configuration import *
from sys import platform as _platform

class BridgeUtils(object):
    
    if _platform == "linux" or _platform == "linux2":
        ConfigurationPaths={"ACG":"./BridgeACG.ini","AIF":"./BridgeAIF.ini"}
    elif _platform == "win32":
        # Windows...
        ConfigurationPaths={"ACG":"../BridgeACG.ini","AIF":"../BridgeAIF.ini"}
    
    
    def __init__(self):
        self.path=""

    def GetParameters(self,label):
        
        path=self.ConfigurationPaths[label]
        #prende il file di configurazione specificato nella classe Configuration
        configuration=Configuration()
        #leggi i parametri dal file di configurazione a seconda della label
        configuration.ReadConfigurationFromFile(path)
        Object_Label=Configuration.IPAddressMap[label]
        return Object_Label
    
    def GetAddress(self,label):
        Object=self.GetParameters(label)       
        port=Object.Port
        IP=Object.IP
        Address=(IP,port)
        return Address
