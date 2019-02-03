from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
print(s.send(b'Hello'))
print(s.recv(8192))