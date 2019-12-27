#!/usr/bin/env python3

import sys
import socket
import re

class Mapper:
    def __init__(self):
        # initial code
        self.count = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        
    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)
                
    def map(self):
        for line in sys.stdin:
            line = line.strip()
            line = re.sub('[.,:;?!|]', '', line)
            words = line.split()
            two_words = None
            last_word = None
            
            for word in words:
                if last_word:
                    two_words = last_word + ' ' + word
                    print('{}\t{}'.format(two_words, 1))
                last_word = word

# Main

def main(argv):
    mapper = Mapper()
    mapper.map()

if __name__ == "__main__":
    main(sys.argv[:1])