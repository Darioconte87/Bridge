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
        self.addr=(self.m_localIPAddress,self.m_localPort)
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
            print ("Socket Client successfully created")
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
    
    def Close(self):
        if (self.m_socket >= 0):
            self.m_socket.close()
            ClientTCP.__init()
    
Server=ClientTCP()
Server.OpenClient("127.0.0.1", 15000)
Server.Send("HOLAAAAA")
msg=Server.Receive()
print("messaggio ricevuto in echo dal bridge %s" %msg)