'''
Created on 20 lug 2015

@author: DarioConte
'''
from threading import Thread

class MyThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.bRunning=False
        
    #metodo che sara sovrascritto dalle funzioni    
    def run(self):
        if(self.bRunning==True): 
            return
        self.bRunning=True
        print("Creazione %s"%self.getName())
  
    def stop(self):
        if(self.bRunning==False):
            return;
        self.bRunning = False;
        self.t.join()