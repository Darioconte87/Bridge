'''
Created on 13 lug 2015

@author: DarioConte
'''

from IPAddressConfiguration import *
from locale import atoi

class Configuration:
    
    
    COMMENT_TAG = "//"
    LABEL_TAG = "Label"
    IP_TAG = "IPAddress"
    PORT_TAG = "Port"
    IPAddressMap={}
    
    def __init__(self): 
        self.Line = ""
        self.LineNumber = 0
        self.PATH_CONFIGURATION_FILE=""
        
    def ReadConfigurationFromFile(self,path):
        self.PATH_CONFIGURATION_FILE=path
        
        try:
            #apro in lettura il file di configurazione
            
            f = open(self.PATH_CONFIGURATION_FILE, 'r')
        except:
            print("File di configurazione non trovato")
             
        
        #leggo riga per riga il file di configurazione
        for self.Line in f:
            
            #ignoro i commenti
        
            if(self.ReadNextLine(f)):
 
                #SingleLine[0]=primo campo
                #SingleLine[1]=campo valore     
                               
                SingleLine=self.split()     
                          
                if(SingleLine[0].lower()==Configuration.LABEL_TAG.lower()):
                    
                    # creo un oggetto IPAddressConfiguration che memorizzera' le informazioni estratte dal file di configurazione 
        
                    ipAddress = IPAddressConfiguration()
                    
                    #assegna alla mappa di AIF o ACG il corrispettivo oggetto di configurazione
                    Configuration.IPAddressMap[SingleLine[1]]=ipAddress
                    
                elif(SingleLine[0].lower()==Configuration.IP_TAG.lower()):   
                    ipAddress.IP=SingleLine[1]
                elif(SingleLine[0].lower()==Configuration.PORT_TAG.lower()):
                    ipAddress.Port=atoi(SingleLine[1])
        f.close()        
        
    def split(self):
        #splitta la stringa in due campi (LABEL e VALORI)
        SingleLine=self.Line.split(":")
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
        bufferL=""
        
        for i in range(0,len(self.Line)):
            if(self.Line[i]!=' ') and (self.Line[i]!='\t') and (self.Line[i]!='\n'):
                bufferL+=self.Line[i]
        self.Line=bufferL