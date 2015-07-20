'''
Created on 20 lug 2015

@author: DarioConte
'''
from MyThread import *

class TCPSimulatorThread(MyThread):

    def __init__(self, label,ip,port,multicast,message_type,socket_type):
        self.m_label=label
        self.m_ip=ip
        self.m_port=port
        self.m_multicast=multicast
        self.m_message_type=message_type
        self.m_socketType=socket_type
        
    def run(self):
        print("ciao")
    
        