import socket
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('\nVocê está conectado!\n\nPara sair use CTRL+X')
msg = input('\n')
while msg != '\x18':
    udp.sendto(msg.encode(), dest)
    msg = input('\n')
udp.close()
