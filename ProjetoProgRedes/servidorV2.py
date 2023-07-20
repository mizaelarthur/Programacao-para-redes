import socket
import threading

# Define o host e porta do servidor
HOST = '0.0.0.0'
PORTA = 12345

# Dicionário para armazenar as mensagens enviadas pelos clientes
mensagens_enviadas = {}

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            
            # Separa o comando e os parâmetros da mensagem
            comando, *parametros = data.strip().split(':')
            
            # Implementação dos comandos
            if comando == '/q':
                client_socket.send('Saindo...'.encode('utf-8'))
                break
            
            elif comando == '/l':
                client_socket.send(str(mensagens_enviadas).encode('utf-8'))
            
            elif comando == '/m':
                ip_destino, porta_destino, mensagem = parametros
                key = f'{ip_destino}:{porta_destino}'
                if key in mensagens_enviadas:
                    mensagens_enviadas[key].append(mensagem)
                else:
                    mensagens_enviadas[key] = [mensagem]
                client_socket.send('Mensagem enviada com sucesso.'.encode('utf-8'))
            
            # Implemente os outros comandos aqui
            
            else:
                client_socket.send('Comando inválido.'.encode('utf-8'))
        
        except Exception as e:
            print(f'Erro: {e}')
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))
    server.listen(5)
    print(f'Servidor escutando em {HOST}:{PORTA}')

    while True:
        client_socket, addr = server.accept()
        print(f'Conexão estabelecida com {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()
