'''
Created on 07 ago 2015

@author: DarioConte
'''

from socket import *
import select
import time
import json


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
        b = json.dumps(msg).encode('utf-8')
        self.m_socket.sendall(b)
        print("Messaggio mandato con successo")
        
    def Close(self):
        if (self.m_socket >= 0):
            self.m_socket.close()
            InterfaceUtils.__init()
