#!/usr/bin/env python3

import socket
import sys


class Socket2Console:
    def __init__(self):
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to the port
        self.server_address = ('localhost', 10000)
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)

    def data2Console(self):
        while True:
            data, address = self.sock.recvfrom(4096)
            print('{}: {}'.format(address, data.decode('utf-8').rstrip()))


# Main

def main(argv):
    sock2Console = Socket2Console()
    sock2Console.data2Console()


if __name__ == "__main__":
    main(sys.argv[:1])
