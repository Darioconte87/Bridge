'''
Created on 20 lug 2015

@author: DarioConte
'''
from MyThread import *
from SocketTCP import *

class TCPSimulatorThread(MyThread):
    
    Client="Client"
    
    def __init__(self, label,ip,port,multicast,message_type,socket_type):
        MyThread.__init__(self)
        self.m_label=label
        self.m_ip=ip
        self.m_port=port
        self.m_multicast=multicast
        self.m_message_type=message_type
        self.m_socketType=socket_type
    
    def run(self):
        MyThread.run(self)
        #creo la socket per la comunicazione
        #PARTE SERVER
        #print("CONFIGURAZIONE SERVER")
        EchoServer(self.m_ip, int(self.m_port))
        asyncore.loop()
                
                
    def isRunning(self):
        return self.bRunning
    
'''               
simulatore=TCPSimulatorThread("ACG","127.0.0.1","5001",False,"0",False)
simulatore.start()
simulatore.stop()'''
