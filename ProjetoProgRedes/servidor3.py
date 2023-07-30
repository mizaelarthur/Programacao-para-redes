import socket
import threading
import feedparser

# Lista para armazenar as mensagens enviadas por cada cliente
historico_mensagens = {}

# Lista para armazenar os clientes conectados
clients = []

# Função para tratar as conexões dos clientes individualmente
def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Tratamento dos comandos
        if data == "/q":
            print(f"Cliente {client_address} desconectado.")
            client_socket.close()
            clients.remove(client_socket)
            return
        elif data == "/l":
            response = "\n".join(f"{addr[0]}:{addr[1]}" for addr in clients)
            client_socket.send(response.encode('utf-8'))
        elif data.startswith("/m:"):
            _, dest_ip, dest_port, message = data.split(":", 3)
            dest_port = int(dest_port)
            message = message.strip()
            send_message(dest_ip, dest_port, message)
        elif data.startswith("/b:"):
            message = data.split(":", 1)[1].strip()
            broadcast_message(client_socket, message)
        elif data == "/h":
            response = "\n".join(historico_mensagens.get(client_socket, []))
            client_socket.send(response.encode('utf-8'))
        elif data == "/?":
            response = "Comandos disponíveis:\n/q - Desconectar\n/l - Listar clientes conectados\n/m:{ip}:{porta}:{mensagem} - Enviar mensagem para cliente específico\n/b:{mensagem} - Enviar mensagem para todos os clientes\n/h - Histórico de mensagens\n/? - Ajuda\n/rss:{palavra_chave} - Buscar notícias com base na palavra-chave"
            client_socket.send(response.encode('utf-8'))
        elif data.startswith("/rss:"):
            keyword = data.split(":", 1)[1].strip()
            news = get_rss_news(keyword)
            response = "\n".join(news)
            client_socket.send(response.encode('utf-8'))
        else:
            # Caso o comando não seja reconhecido
            response = "Comando inválido. Digite /? para ver os comandos disponíveis."
            client_socket.send(response.encode('utf-8'))

        # Armazenar mensagem no histórico
        historico_mensagens.setdefault(client_socket, []).append(data)

    client_socket.close()

# Função para enviar mensagem para um cliente específico
def send_message(dest_ip, dest_port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((dest_ip, dest_port))
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Erro ao enviar mensagem para {dest_ip}:{dest_port}: {e}")

# Função para enviar mensagem para todos os clientes, exceto o remetente
def broadcast_message(sender_socket, message):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Erro ao enviar mensagem para cliente: {e}")

# Função para buscar notícias com base na palavra-chave utilizando feeds RSS
def get_rss_news(keyword):
    url = f"https://news.google.com/rss/search?q={keyword}"
    feed = feedparser.parse(url)
    news_list = []

    for entry in feed.entries[:10]:
        title = entry.title
        link = entry.link
        news_list.append(f"{title}: {link}")

    return news_list

# Configurações do servidor
server_ip = '0.0.0.0'
server_port = 12345

# Inicialização do socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

print(f"Servidor escutando em {server_ip}:{server_port}")

# Loop principal do servidor para aceitar conexões
while True:
    client_socket, client_address = server.accept()
    print(f"Cliente {client_address} conectado.")
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
