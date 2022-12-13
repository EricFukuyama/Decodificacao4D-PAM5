import socket
import time 

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('DESKTOP-DHNLUU3',7777))

    def ler_mensagem(self):
        data = self.client.recv(1123456).decode()
        return data