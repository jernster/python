from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)

s.sendto(b'', ('localhost',40000))

print(s.recvfrom(8192))