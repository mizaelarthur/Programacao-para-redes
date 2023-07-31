import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
    except Exception as e:
        print(f"Erro na conexão: {e}")
    finally:
        client_socket.close()

def send_command():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = ('127.0.0.1', 8888)
        client_socket.connect(server_address)

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            command = input("\n\nDigite um comando ('/?' para ajuda):\n>>> ")
            client_socket.send(command.encode('utf-8'))

            if command == "/q":
                break
    except Exception as e:
        print(f"Erro na conexão: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    send_command()
