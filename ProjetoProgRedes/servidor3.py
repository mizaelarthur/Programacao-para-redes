import socket
import threading

# Lista para armazenar as conexões ativas e seus respectivos históricos
connections = {}
# Arquivo de log
log_file = "server_log.txt"

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Adiciona a mensagem ao histórico do cliente
            connections[client_address].append(data)

            # Processa o comando do cliente
            if data.startswith('/q'):
                client_socket.sendall(b"Desconectando...")
                del connections[client_address]
                break
            elif data.startswith('/l'):
                msg = "\n".join([f"{addr[0]}:{addr[1]}" for addr in connections.keys()])
                client_socket.sendall(msg.encode('utf-8'))
            elif data.startswith('/m:'):
                _, dest_ip, dest_port, message = data[3:].split(':', 3)
                dest_address = (dest_ip, int(dest_port))
                if dest_address in connections:
                    connections[dest_address].append(f"De {client_address[0]}:{client_address[1]}: {message}")
                    client_socket.sendall(b"Mensagem enviada.")
                else:
                    client_socket.sendall(b"Destinatario nao encontrado.")
            elif data.startswith('/b'):
                message = f"De {client_address[0]}:{client_address[1]} para todos: {data[3:]}"
                for address, conn in connections.items():
                    conn.append(message)
            elif data.startswith('/h'):
                msg = "\n".join(connections[client_address])
                client_socket.sendall(msg.encode('utf-8'))
            else:
                client_socket.sendall(b"Comando invalido.")
        except Exception as e:
            print(f"Erro: {e}")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    print("[INFO] Servidor iniciado.")

    while True:
        client_socket, client_address = server_socket.accept()
        connections[client_address] = []
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def main():
    start_server()

if __name__ == "__main__":
    main()
