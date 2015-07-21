'''
Created on 20 lug 2015

@author: DarioConte
'''
from MyThread import *
from SocketTCP import *

class TCPSimulatorThread(MyThread):
    
    Client="Client"
    
    def __init__(self, label,ip,port,multicast,message_type,socket_type):
        self.m_label=label
        self.m_ip=ip
        self.m_port=port
        self.m_multicast=multicast
        self.m_message_type=message_type
        self.m_socketType=socket_type
        
    def m_Run(self):
        
        MyThread.m_Run(self)
        #creo la socket per la comunicazione
        
        Socket=SocketTCP()
        
        if(self.m_socketType==self.Client):
            #PARTE CLIENT
            print("CONFIGURAZIONE CLIENT")
            Socket.OpenClient(self.m_ip, int(self.m_port))
        else:
            #PARTE SERVER
            print("CONFIGURAZIONE SERVER")
            Socket.OpenServer(self.m_ip, int(self.m_port))
            #si mette in attesa di un messaggio da parte di ACG
            print("Messaggio ricevuto da ACG")
        while(self.isRunning()):
            if(self.m_socketType=="Server"):
                
                msg=Socket.Receive()
                #qui gestisci il messaggio ricevuto da ACG
                #ora diventa client ed invia il messaggio ad AIF
                print("invio nuovamente questo messaggio ad ACG: %s" %msg)
                
    
    def isRunning(self):
        return MyThread.bRunning
    '''           
simulatore=TCPSimulatorThread("ACG","127.0.0.1","5777",False,"0",False)
simulatore.start()
simulatore.stop()'''