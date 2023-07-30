import socket

server_ip = '127.0.0.1'  # Altere para o IP do servidor
server_port = 12345  # Altere para a porta do servidor

# Função para receber mensagens do servidor
def receive_message(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)

# Configuração do socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# Iniciando thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive_message, args=(client,))
receive_thread.start()

# Loop principal para enviar comandos ao servidor
while True:
    command = input()
    client.send(command.encode('utf-8'))

    if command == "/q":
        print("Desconectando...")
        client.close()
        break
