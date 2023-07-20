import socket

# Define o host e porta do servidor
HOST = 'localhost'
PORTA = 12345

def send_message(client_socket, message):
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORTA))

    while True:
        message = input('Digite um comando: ')
        send_message(client_socket, message)

        if message == '/q':
            break

    client_socket.close()

if __name__ == '__main__':
    main()
