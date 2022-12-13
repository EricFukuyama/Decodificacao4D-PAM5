import socket
import time 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('DESKTOP-SVH7C0A',7777))

while True:
    data = client.recv(1123456).decode()
    if(data == 'close'):
        client.close()
        break
    print(data)
    if not data:
        break
