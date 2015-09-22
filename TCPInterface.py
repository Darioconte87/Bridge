'''
Created on 22 lug 2015

@author: DarioConte

CLASSE DI CONFIGURAZIONE DEL BRIDGE
'''

from MyThread import MyThread
from TCPSimulatorThread import TCPSimulatorThread
from BridgeUtils import BridgeUtils

class TCPInterface(MyThread):

    def __init__(self, label):
        MyThread.__init__(self)
        self.label=label
        self.bridgeutil=BridgeUtils()
        
    def run(self):
        MyThread.run(self)
        Object_Label=self.bridgeutil.GetParameters(self.label)
        print("Metto in ascolto l'interaccia %s su %s: %s \n" %(self.label,Object_Label.IP,Object_Label.Port)) 
        thread=TCPSimulatorThread(self.label,Object_Label.IP,Object_Label.Port)
        thread.start()
        