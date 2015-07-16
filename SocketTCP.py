'''
Created on 15 lug 2015

@author: DarioConte
'''
from socket import *

class SocketTCP:
    
    def __init__(self):
        self.m_socket = -1
        self.m_localPort = -1
        self.m_multicast = False
        self.m_joined = False
        self.m_localIPAddress=""
        self.m_socketType=False
        self.addr = ()
        
    def OpenServer(self,ipAddress,port,multicast):
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        self.m_multicast=multicast
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            m_lsocket = socket(AF_INET, SOCK_STREAM)
            print ("Socket successfully created")
        except OSError as err:
            print ("socket creation failed with error %s" %(err))
            exit(0)
        self.addr=(self.m_localIPAddress,self.m_localPort)
        try:
            m_lsocket.bind(self.addr)
        except m_lsocket.error as err:
            print("SocketTCP::bind failed with error: %s" %err)
        try:
            m_lsocket.listen(5)
            print("Socket now listening")
        except m_lsocket.error as errlist:
            print("SocketTCP::listen failed with error %s" %errlist)
        
        self.m_socket, clientaddr = m_lsocket.accept()
        print("SocketTCP::accept OK")
        self.m_socketType=True
        print("SocketTCP:Connect OK")
        
    
    def OpenClient(self,ipAddress,port,multicast):
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        self.m_multicast=multicast
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            self.m_socket = socket(AF_INET, SOCK_STREAM)
            print ("Socket successfully created")
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
            SocketTCP.__init()
    
Server=SocketTCP()
Server.OpenServer("localhost", 5777, False)       