'''
Created on 03 ago 2015

@author: DarioConte
'''
from AcgMessages import *
from AifMessages import *
from InterfaceUtils import *
from Utilities import *
import time
import copy

class AIFTest(object):

    maRealeAtn=copy.deepcopy(AcgMobileAddress)
    maRealeFANS=copy.deepcopy(AcgMobileAddress)

    def __init__(self):
        self.maRealeAtn["m_addressType"]=self.maRealeAtn["m_addressType"].acg_mobileAddress24bit
        self.maRealeAtn["AcgMobileAddress_u"]["m_aircraftAddress24"]=1
        self.maRealeFANS["m_addressType"]=self.maRealeFANS["m_addressType"].acg_mobileAddressRegistrationNumber
        self.maRealeFANS["AcgMobileAddress_u"]["m_address"]="FANS"
        #da appprofondire per ora lascio cosi
        self.csSim="FLX0    "
        self.Incremental_MID = 2

    def StartUpMasterOperative(self):
        #inizializza le strutture dati
        #aif=AIFTest()
        
        #SALTO FASE DI ALLINEAMENTO CDB....
        
        print("AIF in ascolto")
        Cdb=InterfaceUtils()
        Cdb.OpenAIFInterface()

        #PROVA COMUNICAZIONE ACG-AIF CON LE STRUTTURE DATI
        
        print("CDB:Invio sys info...")
        infoMsg=copy.deepcopy(MsgToSend)
        infoMsg["messaggio"]["Des"]=18
        infoMsg["messaggio"]["wSize"]=1 
        infoMsg["messaggio"]["FdpStatus"]=1
        infoMsg["messaggio"]["MSTStatus"]=1
        infoMsg["messaggio"]["SLVStatus"]=0
        infoMsg["messaggio"]["latDegrees"]=17
        infoMsg["messaggio"]["latMinutes"]=8
        infoMsg["messaggio"]["latSeconds"]=0
        infoMsg["messaggio"]["latOri"]=78
        infoMsg["messaggio"]["longDegrees"]=78
        infoMsg["messaggio"]["lonMinutes"]=22
        infoMsg["messaggio"]["lonSeconds"]=0
        infoMsg["messaggio"]["lonOri"]=69
        
        print("CDB: Invio sys info...")
        #manda messaggio ad AIF
        Cdb.sendmsg(infoMsg)
        print("CDB: sys info inviato!!")
        print("ACG: Connessione con ACG....")     
        
        time.sleep(200)
        
        
        '''
        services=copy.deepcopy(AcgMsgToSend)
        Cdb.OpenACGInterface()
        print("ACG: receive offered services...")
        print("ACG: Offered services received")
        Cdb.sendmsg(services)
        '''
        '''
        utilities=Utilities()
        utilities.azzeraMessaggio(services)
        
        #building offered services
        services["data"]["buffer"]=1 #tutti i servizi sono abilitati
        services["data"]["messaggio"]["m_callback"]=126 #cb_registerCallback
        
        
        time.sleep(100)
        '''
       
aif=AIFTest()
aif.StartUpMasterOperative()