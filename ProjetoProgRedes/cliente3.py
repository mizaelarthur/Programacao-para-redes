import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8888))

    while True:
        command = input("Digite um comando (/q para sair): ")
        s.sendall(command.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(data)

    s.close()

if __name__ == "__main__":
    main()
