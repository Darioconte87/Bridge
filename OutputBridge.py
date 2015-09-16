'''
Created on 16 set 2015

@author: DarioConte
'''

class OutputBridge(object):

    BASE_HEX=16
    
    def __init__(self, buffer):
        self.string=buffer
    
    """ Dividi il messaggio ricevuto in gruppi da 32 caratteri"""
        
    def split_string(self):
        chunk_size=self.BASE_HEX*2
        x=[self.string[i:i+chunk_size] for i in range(0, len(self.string), chunk_size) ]
        return x
    
    """ Formattazione della stringa ricevuta come sequena valori lunghi nbytes separati da spazi."""
         
    def format_hex(self,string_chunk,nbytes):
        chars_item=nbytes*2
        num_chunks=len(string_chunk)
        def chunkify(self):
            for start in xrange(0,len(string_chunk),chars_item):
                yield string_chunk[start:start+chars_item]
        return ' '.join(chunkify(self))
    
    """ Formatta l'output del Bridge in modo da mostrare la codifica esadecimale in gruppi di byte e relativa codifica"""
    
    def print_output(self,string_chunk):
        
        for i in range(0,len(string_chunk)):
            
            space_right=self.calculate_right_space(string_chunk[i]) 
            decode_string=string_chunk[i].decode("hex")
            
            print(format(i, "03d")+": "+self.format_hex(string_chunk[i],1) + " " + decode_string.rjust(space_right," ") )
    
    """ Funzione che allinea il testo decodificato nel caso in cui gli esadecimali non completino tutta la riga"""
            
    def calculate_right_space(self,string_chunk):
        len_string=self.count_string_hex(string_chunk)
        if(len_string==32):
            right_space=20
        else: right_space=48
        return right_space
    
    def count_string_hex(self, string_chunk):
        count=len(string_chunk)
        return count
        