import socket, threading

# Defininindo endereço e Porta do Servidor
SERVER = '0.0.0.0'
PORT = 5678

# Criei uma função para interação de mensagem. Caso o cliente digite "/q" ele encerra o socket.
def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'/q':
        try:
            msg = sockConn.recv(512)
            broadCast (msg, addr)
        except:
            msg = b'/q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

