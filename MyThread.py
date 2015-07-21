'''
Created on 20 lug 2015

@author: DarioConte
'''
import threading

class MyThread(object):
    
    bRunning=False
    ThreadId=0
    
    def __init__(self,t):
        self.t=t
        
    def start(self):    
        if(MyThread.bRunning==True): 
            return
        MyThread.bRunning=True
        #creo il thread e richiamo il metodo M_run
        self.t = threading.Thread(target=self.m_Run)
        print("Creo nuovo thread per gestire la chiamata: %s"%self.t.getName())
        self.t.start()     
    
    #metodo che sara sovrascritto dalle funzioni    
    def m_Run(self):
        pass
        
    def stop(self):
        if(MyThread.bRunning==False):
            return;
        MyThread.bRunning = False;
        self.t.join()