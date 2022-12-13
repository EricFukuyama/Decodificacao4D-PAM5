import socket 

class Servidor:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        print(hostname)
        self.server.bind((hostname,7777))
        self.server.listen(2)
        self.connection, self.addresss = self.server.accept()
        
    def mandar_mensagem(self,mensagem):
        try:
            self.connection.send(bytes(mensagem,'UTF-8'))
        except:
            self.connection,self.addresss = self.server.accept()

    