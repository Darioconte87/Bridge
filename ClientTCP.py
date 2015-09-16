'''
Created on 15 lug 2015

@author: DarioConte

Subject: ECHO CLIENT
'''
from socket import *
import select
import time

try:
    import cPickle as pickle
except ImportError:
    import pickle


class ClientTCP:
    
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
                    
    def Send_Structure(self, msg):
        b = pickle.dumps(msg)
        self.m_socket.sendall(b)
        print("Messaggio mandato con successo")
        self.Close()
    
    def Send(self, buffer):
        totalsent=0
        while totalsent<len(buffer):
            sent=self.m_socket.send(buffer)
            if (sent==0):
                raise RuntimeError("SocketTCP::sendto failed")
            totalsent=totalsent+sent
        
    def Close(self):
            self.m_socket.close()
            
            
'''
Server=ClientTCP()
Server.OpenClient("192.168.0.76", 15000)
'''
"""                       
Server=ClientTCP()
#Server.OpenClient("127.0.0.1", 5001)
#Server.OpenClient("192.168.48.130", 15000)
Server.OpenClient("127.0.0.1", 8080)
Server.Send("Hola..come estas? ")


reply=Server.ReceiveWithTimeout()
print("reply da AIF passando per il bridge %s"%reply)
"""
