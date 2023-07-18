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

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))


try:
    allSocks = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))

    print ("Listening in: ", (SERVER, PORT))
    sock.listen()
