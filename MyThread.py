'''
Created on 20 lug 2015

@author: DarioConte
'''

from threading import Thread

class MyThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    #metodo che sara sovrascritto dalle funzioni    
    def run(self):
        pass
    
    def stop(self):
        self.join()