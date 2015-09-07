'''
Created on 03 ago 2015

@author: DarioConte

ECHO SERVER
'''

from ClientTCP import *
from InterfaceUtils import *
import asyncore
import socket
import json



class SocketTCP(asyncore.dispatcher_with_send):

    def __init__(self,sock,whoiam,source_port):
        asyncore.dispatcher.__init__(self,sock=sock);
        self.out_buffer = ''
        self.source_port=source_port
        self.whoiam=whoiam
          
    def handle_read(self):
        data = b''
        tmp = self.recv(4096)
        data += tmp
        msg = json.loads(data.decode('utf-8'))    
        #Confrontando il valore di porta, si smista il messaggio verso AIF o ACG o si memorizza
        self.dispatcher(msg)
        self.close()
    
    def handle_close(self):
        self.close()
        
    def dispatcher(self,msg):
        
        
        Cdb=InterfaceUtils()
        AifAddress=Cdb.GetAddress("AIF")
        Aif_IP=AifAddress[0]
        Aif_port=AifAddress[1]
        AcgAddress=Cdb.GetAddress("ACG")
        Acg_IP=AcgAddress[0]
        Acg_port=AcgAddress[1]
        
        Acg_port_send=Acg_port+1
        Aif_port_send=Aif_port+1
        
        #AIF
        if(self.whoiam==Aif_port and self.source_port!=Acg_port_send):
            #invia messaggio ad ACG
            Acg=ClientTCP()
            Acg.OpenClient("127.0.0.1", Acg_port,Aif_port_send)
            Acg.Send_Structure(msg)
            print("Messaggio inviato ad ACG")
        elif(self.whoiam==Aif_port and self.source_port==Acg_port_send):
            print("Messaggio ricevuto da ACG")
            print("DEBUG: Stampa valore latDegrees contenuto nel messaggio: %d" %(msg["messaggio"]["latDegrees"])) 
            print("Faro' qualcosa ....")
        #ACG
        elif(self.whoiam==Acg_port and self.source_port!=Aif_port_send):
            #invio messaggio ad AIF
            Aif=ClientTCP()
            Aif.OpenClient("127.0.0.1", Aif_port,Acg_port_send)
            Aif.Send_Structure(msg)
            print("Messaggio inviato ad AIF")
        elif(self.whoiam==Acg_port and self.source_port==Aif_port_send):
            print("Messaggio ricevuto da AIF")
            print("DEBUG: Stampa valore latDegrees contenuto nel messaggio: %d" %(msg["messaggio"]["latDegrees"])) 
            print("...faro' qualcosa...")
                
class EchoServer(asyncore.dispatcher):
    
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        print("SocketTCP::listen OK")
        self.port=port #porta in ascolto
        
    def handle_accept(self):
        pair = self.accept()
        print("SocketTCP::accept OK")
        if pair is not None:
            sock, addr = pair
            print ("Incoming connection from %s" %repr(addr))
            handler = SocketTCP(sock,self.port,addr[1])
            
"""
server = EchoServer('localhost', 8080)
asyncore.loop()
"""