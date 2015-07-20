'''
Created on 13 lug 2015

@author: DarioConte
'''

from IPAddressConfiguration import *
from locale import atoi

class Configuration:
    
    
    COMMENT_TAG = "//"
    LABEL_TAG = "Label"
    SOCKET_TYPE_TAG = "Type"
    SOCKET_TYPE_CLIENT_VALUE = "CLIENT"
    SOCKET_TYPE_SERVER_VALUE = "SERVER"
    IP_TAG = "IPAddress"
    PORT_TAG = "Port"
    MULTICAST_TAG = "Multicast"
    MULTICAST_YES_VALUE = "yes"
    MULTICAST_NO_VALUE = "no"
    MESSAGE_TYPE_TAG = "MessageType"
    IPAddressMap={}
    
    # Path di default
    
    PATH_CONFIGURATION_FILE = "..\Bridge.ini"
    
    def __init__(self): 
        self.Line = ""
        self.LineNumber = 0
    
    def set_Path(self, s):
        self.PATH_CONFIGURATION_FILE = s
        
    def ReadConfigurationFromFile(self):
        
        try:
            #apro in lettura il file di configurazione
            
            f = open(Configuration.PATH_CONFIGURATION_FILE, 'r')
        except:
            print("File di configurazione non trovato")
             
        
        #leggo riga per riga il file di configurazione
        for self.Line in f:
            
            #ignoro i commenti
        
            if(self.ReadNextLine(f)):
                
                SingleLine=self.split()     
                #SingleLine[0]=primo campo
                #SingleLine[1]=campo valore     
                          
                if(SingleLine[0].lower()==Configuration.LABEL_TAG.lower()):
                    
                    # creo un oggetto IPAddressConfiguration che memorizzera' le informazioni estratte dal file di configurazione 
        
                    ipAddress = IPAddressConfiguration()
                    
                    #ATTENZIONE: DEVO INSERIRE IL VALORE DELLA LABEL NELL'ADDRESS-->DA CONFIGURARE
                    #assegna valore della label ad un valore
                    Configuration.IPAddressMap[SingleLine[1]]=ipAddress
                    
                elif(SingleLine[0].lower()==Configuration.SOCKET_TYPE_TAG.lower()):    
                    if((SingleLine[1].lower()==Configuration.SOCKET_TYPE_CLIENT_VALUE.lower())):
                        ipAddress.SocketType=SingleLine[1]
                    elif (SingleLine[1].lower()==Configuration.SOCKET_TYPE_SERVER_VALUE.lower()):
                        ipAddress.SocketType=SingleLine[1]
                    else:
                        self.AbortExecution()    
                elif(SingleLine[0].lower()==Configuration.SOCKET_TYPE_TAG.lower()):   
                    if(SingleLine[1].lower()==Configuration.SOCKET_TYPE_CLIENT_VALUE.lower()):
                        ipAddress.SocketType=SingleLine[1]
                    elif (SingleLine[1].lower()==Configuration.SOCKET_TYPE_SERVER_VALUE.lower()):
                        ipAddress.SocketType=SingleLine[1]
                    else:
                        self.AbortExecution() 
                elif(SingleLine[0].lower()==Configuration.IP_TAG.lower()):   
                    ipAddress.IP=SingleLine[1]
                elif(SingleLine[0].lower()==Configuration.PORT_TAG.lower()):
                    ipAddress.Port=atoi(SingleLine[1])
                elif(SingleLine[0].lower()==Configuration.MULTICAST_TAG.lower()):
                    value=SingleLine[1].lower()
                    if(value==Configuration.MULTICAST_YES_VALUE.lower()):
                        ipAddress.Multicast=True
                    elif(value==Configuration.MULTICAST_NO_VALUE):
                        ipAddress.Multicast=False
                    else:
                        self.AbortExecution()
                elif(SingleLine[0].lower()==Configuration.MESSAGE_TYPE_TAG.lower()):        
                        ipAddress.MessageType=atoi(SingleLine[1])
                else:
                    self.AbortExecution()    
         
        f.close()        
    #CHECK 
    '''          
        print("Type:%s" %ipAddress.SocketType)        
        print("IP:%s" %ipAddress.IP)
        print("Porta %s"%ipAddress.Port)
        print("Multicast %s"%ipAddress.Multicast)
        print("Messagge Type: %s" %ipAddress.MessageType)                    
    '''             
                    
        
        
        
        
        
        
        
    def split(self):
        #splitta la stringa in due campi (LABEL e VALORI)
        SingleLine=self.Line.split(sep=":", maxsplit=1)
        return SingleLine    
        
    def AbortExecution(self):    
        print("Valore non valido: Errore alla riga %d del File di Configurazione" %self.LineNumber)
        exit(0)
        
    def ReadNextLine(self, ConfigurationFile):
        lineRead = False
        self.LineNumber=self.LineNumber+1
        #se la linea contiene un carattere nullo oppure contiene un commento viene ignorata
        if (len(self.Line)==1) or (self.Line[0:2]==Configuration.COMMENT_TAG):
            pass
        else:
            lineRead=True
            #elimina spazi e tabulazioni
            self.TrimLine()
        return lineRead
             
    def TrimLine(self):
        buffer=""
        
        for i in range(0,len(self.Line)):
            if(self.Line[i]!=' ') and (self.Line[i]!='\t') and (self.Line[i]!='\n'):
                buffer+=self.Line[i]
        self.Line=buffer
        
#test di funzionamento della classe        
prova = Configuration()
prova.ReadConfigurationFromFile()
