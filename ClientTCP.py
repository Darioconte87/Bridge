'''
Created on 15 lug 2015

@author: DarioConte
'''
from socket import *
import select
import time
import json


class ClientTCP:
    
    def __init__(self):
        self.m_socket = -1
        self.m_localPort = -1
        self.m_multicast = False
        self.m_joined = False
        self.m_localIPAddress=""
        self.m_socketType=False
        self.addr = ()
        
        
    def OpenClient(self,ipAddress,port,port_send):
        
        self.m_localIPAddress=ipAddress
        self.m_localPort=port
        
        #creazione della socket
        try:
            #crea una AF_INET, STREAM socket (TCP)
            self.m_socket = socket(AF_INET, SOCK_STREAM)
            #print ("Socket Client successfully created")
        except:
            raise Exception ("Socket creation failed")
            exit(0)
        self.addr=(self.m_localIPAddress,self.m_localPort)
        try:
            self.m_socket.bind(("127.0.0.1",port_send)) #questo permette di settare l'indirizzo completo da cui inviare i dati
        except:
            raise Exception("Binding error")
        
        #TIME_WAIT is the state that typically ties up the port for several minutes after the process has completed.
                
        result=self.m_socket.connect_ex(self.addr)
        
        #IMPORTANTE! Questo ciclo garantisce che la connessione effettivamente e' avvenuta con successo
        #BYPASSA il problema del TIME_WAIT
        
        while(result!=0):
            result=self.m_socket.connect_ex(self.addr)
        
        '''    
        try:
            self.m_socket.connect(self.addr)
        except OSError as err:
            raise Exception("Server not in listening. Error: %s" %err)
        '''
        self.m_socketType=False
        print("SocketTCP:Connect OK")            
            
    def Send_Structure(self, msg):
        b = json.dumps(msg).encode('utf-8')
        self.m_socket.sendall(b)
        print("Messaggio mandato con successo")
        self.Close()
        
    def Close(self):
            self.m_socket.close()
            



"""                       
Server=ClientTCP()
#Server.OpenClient("127.0.0.1", 5001)
#Server.OpenClient("192.168.48.130", 15000)
Server.OpenClient("127.0.0.1", 8080)
Server.Send("Hola..come estas? ")


reply=Server.ReceiveWithTimeout()
print("reply da AIF passando per il bridge %s"%reply)
"""
