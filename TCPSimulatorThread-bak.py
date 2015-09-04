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
        
        Socket_ACG=SocketTCP()
        Socket_AIF=SocketTCP()
        
        if(self.m_socketType==self.Client):
            #PARTE CLIENT
            print("CONFIGURAZIONE CLIENT")
            Socket_ACG.OpenClient(self.m_ip, int(self.m_port))
        else:
            #PARTE SERVER
            print("CONFIGURAZIONE SERVER")
            Socket_ACG.OpenServer(self.m_ip, int(self.m_port))
            #si mette in attesa di un messaggio da parte di ACG
            #print("Messaggio ricevuto da ACG")
            msg_client=Socket_ACG.ReceiveWithTimeout()
            print("Client ha inviato al bridge il seguente messaggio: %s " %msg_client)
            #Smista il messaggio all'altra entità in ascolto (uso una classe Thread tipo Dispatcher??)
            Socket_AIF.OpenClient(self.m_ip, 15000)
            #Socket_AIF.OpenClient("192.168.48.130", 15000)
            Socket_AIF.Send(msg_client)
            msg_Aif=Socket_AIF.ReceiveWithTimeout()
            Socket_ACG.Send(msg_Aif)
           
    def isRunning(self):
        return self.bRunning
    
'''               
simulatore=TCPSimulatorThread("ACG","127.0.0.1","5777",False,"0",False)
simulatore.start()
simulatore.stop()'''