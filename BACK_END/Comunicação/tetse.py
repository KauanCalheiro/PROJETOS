import socket

ip_local = socket.gethostbyname(socket.gethostname())
print(type(ip_local))
print(ip_local)