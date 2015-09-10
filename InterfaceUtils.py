'''
Created on 07 ago 2015

@author: DarioConte
Classe di funzione per AIF-ACG
'''

from socket import *
from Configuration import *
import pickle


class InterfaceUtils:
    
    def __init__(self):
        self.m_socket = -1
        self.m_localPort = -1
        self.m_multicast = False
        self.m_joined = False
        self.m_localIPAddress=""
        self.m_socketType=False
        self.addr = ()
    
    def OpenClient(self,ipAddress,port):
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            self.m_socket = socket(AF_INET, SOCK_STREAM)
            
            #print ("Socket Client successfully created")
        except OSError as err:
            print ("Socket creation failed with error %s" %(err))
            exit(0)
        self.addr=(self.m_localIPAddress,self.m_localPort)
        try:
            self.m_socket.connect(self.addr)
        except OSError as err:
            raise Exception("Server not in listening. Error: %s" %err)
        self.m_socketType=False
        print("SocketTCP:Connect OK")            
    
    def sendmsg(self, msg):
        b = pickle.dumps(msg)
        self.m_socket.sendall(b)
        print("Messaggio mandato con successo")
        self.m_socket.close()
    
    def GetAddress(self,label):
        ConfigurationPaths={"ACG":"../BridgeACG.ini","AIF":"../BridgeAIF.ini"}
        path=ConfigurationPaths[label]
        #prende il file di configurazione specificato nella classe Configuration
        configuration=Configuration()
        #leggi i parametri dal file di configurazione a seconda della label
        configuration.ReadConfigurationFromFile(path)
        Object_Label=Configuration.IPAddressMap[label]
        port=Object_Label.Port
        IP=Object_Label.IP
        address=(IP,port)
        return address
        
    def OpenAIFInterface(self):
        AifAddress=self.GetAddress("AIF")
        self.OpenClient(AifAddress[0],AifAddress[1])
    
    def OpenACGInterface(self):
        AcgAddress=self.GetAddress("ACG")
        self.OpenClient(AcgAddress[0],AcgAddress[1])
            
    def Close(self):
        if (self.m_socket >= 0):
            self.m_socket.close()
            InterfaceUtils.__init()
