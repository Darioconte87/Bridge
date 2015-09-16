'''
Created on 03 ago 2015

@author: DarioConte

ECHO SERVER
'''

from ClientTCP import *
from BridgeUtils import *
import asyncore
import socket
import binascii
from OutputBridge import *

try:
    import cPickle as pickle
except ImportError:
    import pickle


class SocketTCP(asyncore.dispatcher_with_send): 
    
    BASE_HEX=16
    
    def __init__(self,sock,source_addr):
        asyncore.dispatcher.__init__(self,sock=sock);
        self.source_addr=source_addr # indirizzo IP sorgente del pacchetto TCP
        self.out_buffer = ''
        self.Address=BridgeUtils()
        
    def handle_read(self):
        
        #ricevi il messaggio
        
        while True:
            try:
                buffer = self.recv(4096)
            except:
                self.close()
                break     
        
        #codifica esadecimale del messaggio
        
        msg=binascii.hexlify(buffer.encode('utf8'))
        
        Id,size=self.ReadHeaderTCP(msg)

        #msg = pickle.loads(tmp) #testo in chiaro
        
        self.dispatcher(msg,size)
        self.close()
    
    def handle_close(self):
        self.close()
    
    def dispatcher(self,msg,size):
        
        #Manda il messaggio ad ACG
        
        if(self.source_addr==self.Address.GetAddress("ACG")[0]):
            print("Messaggio ricevuto da AIF, size: %d" %size)
            self.display(msg)
            Acg=ClientTCP()
            Acg.OpenClient(self.Address.GetAddress("AIF")[0],self.Address.GetAddress("AIF")[1] )
            #serializzo le strutture dati
            Acg.Send_Structure(msg) 
            print("Messaggio inviato ad ACG")   
            
        #Manda il messaggio ad AIF
        
        elif(self.source_addr==self.Address.GetAddress("AIF")[0]):
            print("Messaggio ricevuto da ACG:")
            print(msg)
            Aif=ClientTCP()
            Aif.OpenClient(self.Address.GetAddress("ACG")[0],self.Address.GetAddress("ACG")[1] )
            Acg.Send_Structure(msg)
            print("Messaggio inviato ad AIF")   
            
    def ReadHeaderTCP(self,msg): 
        
        #ricevi i primi 2 byte (1 byte= ID, 2 byte=size)
        
        Id=int(msg[0:2],self.BASE_HEX) #1 byte
        size=int(msg[2:4],self.BASE_HEX) #2 byte
        if (size==0):
            size=int(msg[2:8],self.BASE_HEX) #nel caso di dimensione 4096 
        return Id,size
        
        
        #Funzione per il display del messaggio sul bridge 
    def display(self,msg):
        
        Format_Output=OutputBridge(msg)
        splitted_string=Format_Output.split_string()
        Format_Output.print_output(splitted_string)
        '''
        #numero di righe da generare
        
        N_row=size/self.N_BYTES_ROW
        
        for i in range(0,N_row):
            count=0                 #indice per scorrere la riga
            string=""               
            #costruisci la riga
            for j in range(0,self.BASE_HEX,2):
                print(j)
                print(msg[j])
                #print(msg[j:j+1]+"")
            #print(format(i, "03d")+":")
        '''    

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
            handler = SocketTCP(sock,addr[0])
            