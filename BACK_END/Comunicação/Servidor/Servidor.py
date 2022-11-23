import socket

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

HOST = ip_local  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('\nVocê está conectado!\n\nEsperando usuário...\n')
while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, msg.decode())
udp.close()