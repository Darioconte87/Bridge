'''
Created on 03 ago 2015

@author: DarioConte

'''
import binascii
import select
import sys
import time
from BridgeUtils import BridgeUtils
from OutputBridge import *
import socket

BASE_HEX=16
buffer_size = 8192
delay = 0.0001
Address=BridgeUtils()
AIFAddress=Address.GetAddress("ACG")[0]
AIFport=Address.GetAddress("ACG")[1]
ACGAddress=Address.GetAddress("AIF")[0]
ACGPort=Address.GetAddress("AIF")[1]
forward_to = (ACGAddress,ACGPort)

class Forward:
    def __init__(self):
        try:
            self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print ("Socket ACG: creazione fallita!")
            
    def start(self, host, port):
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception:
            return False

class TheServer:
    input_list = []
    channel = {}

    def __init__(self, host, port):
        
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("SocketBridge ERROR:: Creazione socket fallita!")
            
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server.bind((host, port))
        except:
            print("SocketBridge ERROR:: Indirizzo del Bridge in uso da un processo attivo!")
            print("Uccidi il processo e rimetti in ascolto il bridge\n")
            sys.exit(0)
        
        try:
            self.server.listen(200)
            print("SocketTCP:: listen OK")
        except:
            print("SocketBridge ERROR ::listen fallita")
            
        self.AIFSocket=None
        
    def main_loop(self):
        self.input_list.append(self.server)
        
        while 1:
            time.sleep(delay)
            ss = select.select
            inputready, outputready, exceptready = ss(self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()
                    break
                
                
                #leggo messaggio che proviene da una delle socket connesse
                #Self.s puo essere il riferimento della socket AIF o ACG. Si attiva quando vede dei dati in entrata
                
                try:
                    data=self.s.recv(buffer_size)
                except:
                    if(self.s!=AIFAddress):
                        print("ACG ha chiuso la connessione!! Comunicazione interrotta ..")
                    self.on_close()
                    break                
            
                #E' necessario convertire la stringa ricevuta in bytes per leggere il campo dimensione
                
                msg=self.convert_to_hex(data)
                
                #Estrai Id e recupera la dimensione del messaggio
                Id,size=self.ReadHeaderTCP(msg)
                
                #distingui la sorgente e manda il messaggio all'altro nodo
                self.on_recv(msg, Id, size)
                    
                
    def on_accept(self):
        
        clientsock, clientaddr = self.server.accept()
        clientsock.setblocking(0)
        #memorizza la socket di AIF

        if(clientaddr[0]==AIFAddress):
            self.AIFSocket=clientsock
        
        #Inoltra il messaggio ad ACG
        forward = Forward().start(forward_to[0], forward_to[1])
        
        if forward:
            print clientaddr, "has connected"
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print("Non e' possibile connettersi ad ACG!")
            print("Indirizzo ACG %s e' corretto?? "%ACGAddress)
            print("Se l'indirizzo e' corretto, controlla che ACG sia in listening\n")
            clientsock.close()
            sys.exit(0)
            
    def on_close(self):
        
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]
        sys.exit(0)
        
    def on_recv(self,msg,Id,size):
    
        if(self.s==self.AIFSocket):
            #AIF
            print("\nMessaggio ricevuto da AIF, size = %d "%size)
            print("Messaggio inviato ad ACG")
            
        else:
            #ACG

            print("\nMessaggio ricevuto da ACG")
            print("Message ID = %d"%Id)
            print("Size of Message: %d"%size)
            print("Messaggio inviato ad AIF")
    
        #Veicola il display del messaggio
        self.display(msg)
        
        #invio del messaggio ricevuto verso l'altra socket
        self.channel[self.s].send(msg.decode('hex'))
    
    def ReadHeaderTCP(self,msg): 
        
        #ricevi i primi 2 byte (1 byte= ID, 2 byte=size)
        
        Id=int(msg[0:2],BASE_HEX) #1 byte
        size=int(msg[2:4],BASE_HEX) #2 byte
        if (size==0):
            size=int(msg[2:8],BASE_HEX) #nel caso di dimensione 4096 
        return Id,size
    
    def display(self,msg):
        
        Format_Output=OutputBridge(msg)
        splitted_string=Format_Output.split_string()
        Format_Output.print_output(splitted_string)
    
    def convert_to_hex(self,data):
        #converti il messaggio in esadecimale per preparare la lettura di ID e size del messaggio in arrivo
        msg=binascii.hexlify(data.encode('utf8'))
        return msg