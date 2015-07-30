'''
Created on 15 lug 2015

@author: DarioConte
'''
from socket import *
import select
import time
import threading

class SocketTCP:
    
    def __init__(self):
        self.m_socket = -1
        self.m_localPort = -1
        self.m_multicast = False
        self.m_joined = False
        self.m_localIPAddress=""
        self.m_socketType=""
        self.addr = ()
        
    def OpenServer(self,ipAddress,port):
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            m_lsocket = socket(AF_INET, SOCK_STREAM)
            print ("Socket successfully created")
        except OSError as err:
            print ("socket creation failed with error %s" %(err))
            exit(0)
        self.addr=("0.0.0.0",self.m_localPort)
        try:
            m_lsocket.bind(self.addr)
        except OSError as err:
            print("SocketTCP::bind failed with error: %s" %err)
        try:
            m_lsocket.listen(5)
            print("Socket now listening")
        except m_lsocket.error as errlist:
            print("SocketTCP::listen failed with error %s" %errlist)
        
        self.m_socket, self.addr = m_lsocket.accept()
        print("SocketTCP::Accept OK")
        self.m_socketType="Client"
        print("SocketTCP:Connect OK")
        
    
    def OpenClient(self,ipAddress,port):
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            self.m_socket = socket(AF_INET, SOCK_STREAM)
            print ("Socket successfully created")
        except OSError as err:
            print ("Socket creation failed with error %s" %(err))
            exit(0)
        self.addr=(self.m_localIPAddress,self.m_localPort)
        self.m_socket.connect(self.addr)
        self.m_socketType="Server"
        print("SocketTCP:Connect OK")            
        
    def Send(self, buffer):
        totalsent=0
        while totalsent<len(buffer):
            sent=self.m_socket.send(buffer.encode('ascii'))
            if (sent==0):
                raise RuntimeError("SocketTCP::sendto failed")
            totalsent=totalsent+sent
        print("Message send successfully")
            
    def Receive(self):
        data=self.m_socket.recv(4096)
        if not data:
            raise RuntimeError("SocketTCP::recvfrom failed")
        decoded_data=data.decode('ascii')
        print ("Messaggio Ricevuto: %s" %decoded_data)
        return decoded_data
            
    def ReceiveWithTimeout(self):
        self.m_socket.setblocking(0)
        ready = select.select([self.m_socket], [], [], 120)
        if ready[0]:
            data = self.m_socket.recv(4096)
        decoded_data=data.decode('ascii')
        #print ("Messaggio Ricevuto: %s" %decoded_data)
        return decoded_data
    
    def Close(self):
        if (self.m_socket >= 0):
            self.m_socket.close()
            SocketTCP.__init()
            
    #metodo per consentire al server di rispondere a pi� client
            
    def OpenServer2(self,ipAddress,port):   
        
        self.Close()
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        self.addr=(self.m_localIPAddress,self.m_localPort)
        
        serversocket = socket(AF_INET, SOCK_STREAM)

        serversocket.bind(self.addr)

        serversocket.listen(2)

        while 1:
            print ("Server is listening for connections\n")
            self.m_socket, self.addr = serversocket.accept()
            threading.Thread(target=self.handler, args=(self.m_socket,self.addr)).start()
            print("ritorna?")
        
    def handler(self,clientsocket,clientaddr):
        print ("Accepted connection from one client")
        data = self.Receive()
        
'''         
Server=SocketTCP()
Server.OpenServer2("127.0.0.1", 15000) 
#Server.Send("replica")
'''