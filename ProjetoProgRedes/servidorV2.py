import socket

# Define o host e porta do servidor
HOST = '0.0.0.0'
PORTA = 12345

def mensagem(client_socket, msg):
    client_socket.send(msg.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORTA))

    while True:
        msg = input('Digite um comando: ')
        mensagem(client_socket, msg)

        if msg == '/q':
            break

    client_socket.close()

if __name__ == '__main__':
    main()
