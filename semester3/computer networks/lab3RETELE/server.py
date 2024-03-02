

import socket

SERVER_PORT = 1234
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", SERVER_PORT))
#192.168.182.135
s.listen(5)

while True:
    print("Listening for incoming connections...")

    client_socket, client_addr = s.accept()
    print(f"Incoming connected client from: {client_addr}")


    a = int.from_bytes(client_socket.recv(2), byteorder='big')
    b = int.from_bytes(client_socket.recv(2), byteorder='big')

    suma = a + b
    client_socket.send(suma.to_bytes(2, byteorder='big'))
    client_socket.close()
