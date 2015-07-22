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
        
        SocketIACG=SocketTCP()
        
        if(self.m_socketType==self.Client):
            #PARTE CLIENT
            print("CONFIGURAZIONE CLIENT")
            SocketIACG.OpenClient(self.m_ip, int(self.m_port))
        else:
            #PARTE SERVER
            print("CONFIGURAZIONE SERVER")
            SocketIACG.OpenServer(self.m_ip, int(self.m_port))
            #si mette in attesa di un messaggio da parte di ACG
            #print("Messaggio ricevuto da ACG")
            msg=SocketIACG.Receive()
            print("ACG ha inviato al bridge il seguente messaggio: %s " %msg)
            SocketIACG.Send(msg)
            
        '''
        while(self.isRunning()):
            if(self.m_socketType=="Server"):  
                msg=SocketIACG.Receive()
                self.m_socketType="Client"
                #qui gestisci il messaggio ricevuto da ACG
                #ora diventa client ed invia il messaggio ad AIF
                print("invio nuovamente questo messaggio ad ACG: %s" %msg)
                SocketACG.OpenServer(self.m_ip, int(self.m_port))
                SocketACG.Send(msg)
                msg1=SocketACG.Receive()
                print("Ricevuto su ACG %s" %msg1)
        '''
    def isRunning(self):
        return MyThread.bRunning
'''               
simulatore=TCPSimulatorThread("ACG","127.0.0.1","5777",False,"0",False)
simulatore.start()
simulatore.stop()'''