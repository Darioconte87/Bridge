'''
Created on 20 lug 2015

@author: DarioConte
'''
from threading import Thread

class MyThread(object):
    
    def __init__(self):
        Thread.__init__(self)
        self.thread=Thread()
        
    def start(self):    
        self.thread.start()
        
    def stop(self):
        self.thread.join()
    
    def run(self):
        print("ciao")

