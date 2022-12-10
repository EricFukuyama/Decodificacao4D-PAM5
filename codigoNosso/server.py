import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
print(hostname)

server.bind((hostname,7777))
server.listen(2)

while True:
    connection, addresss = server.accept()
    while True:
        mnsg = input("Digite Mensagem para enviar: ")
        try:
            connection.send(bytes(mnsg,'UTF-8'))
        except:
            connection, addresss = server.accept()
