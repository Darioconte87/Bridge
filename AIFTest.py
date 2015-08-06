'''
Created on 03 ago 2015

@author: DarioConte
'''
from AcgMessages import *
from AifMessages import *
from ClientTCP import *

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
        
        #SALTO FASE DI APERTURA CANALE....DA IMPLEMENTARE
        
        print("AIF in ascolto")
        Acg=ClientTCP()
        Acg.OpenClient("127.0.0.1",15000)
        print("ACG abilitato")

        #PROVA COMUNICAZIONE ACG-AIF CON LE STRUTTURE DATI
        
        print("invio messaggio da ACG verso AIF")
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
        Acg.Send_Structure(infoMsg)
        
aif=AIFTest()
aif.StartUpMasterOperative()
