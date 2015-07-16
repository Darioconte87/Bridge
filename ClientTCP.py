'''
Created on 15 lug 2015

@author: DarioConte
'''
from socket import *

class ClientTCP:
    
    def __init__(self):
        self.m_socket = -1
        self.m_localPort = -1
        self.m_multicast = False
        self.m_joined = False
        self.m_localIPAddress=""
        self.m_socketType=False
        self.addr = ()
        
    
    def OpenClient(self,ipAddress,port,multicast):
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        self.m_multicast=multicast
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            self.m_socket = socket(AF_INET, SOCK_STREAM)
            print ("Socket Client successfully created")
        except OSError as err:
            print ("socket creation failed with error %s" %(err))
            exit(0)
        self.addr=(self.m_localIPAddress,self.m_localPort)
        self.m_socket.connect(self.addr)
        self.m_socketType=False
        print("SocketTCP:Connect OK")            
        
    def Close(self):
        if (self.m_socket >= 0):
            self.m_socket.close()
            ClientTCP.__init()
    
Server=ClientTCP()
Server.OpenClient("localhost", 5777, False)