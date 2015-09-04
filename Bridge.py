'''
Created on 21 lug 2015

@author: DarioConte
'''

from TCPInterface import *

if __name__ == '__main__':
    
    print("Avvio del Bridge")
    AvvioInterfacciaACG=TCPInterface("ACG")
    AvvioInterfacciaACG.start()