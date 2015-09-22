'''
Created on 20 lug 2015

@author: DarioConte
'''
from MyThread import MyThread
from SocketTCP import TheServer
import sys

class TCPSimulatorThread(MyThread):
    
    Client="Client"
    
    def __init__(self, label,ip,port):
        MyThread.__init__(self)
        self.m_label=label
        self.m_ip=ip
        self.m_port=port
    
    def run(self):
        MyThread.run(self)
        #creo la socket per la comunicazione
        #PARTE SERVER
        #print("CONFIGURAZIONE SERVER")

        server = TheServer(self.m_ip, int(self.m_port))
        try:
            server.main_loop()
        except KeyboardInterrupt:
            print "Ctrl C - Stopping server"
            sys.exit(1)        
                
    def isRunning(self):
        return self.bRunning
    
'''               
simulatore=TCPSimulatorThread("ACG","127.0.0.1","5001",False,"0",False)
simulatore.start()
simulatore.stop()'''
