import requests
import os



from telegram import envia_msg_telegram
from log import registra_log
from servidor import clients
from rss_config import noticia_rss



def comandos(client_socket, address):
    try:
        # Notificar o Telegram sobre a nova conexão
        message = f"Nova conexão: Cliente {address[0]}:{address[1]} conectado."
        envia_msg_telegram(message)
        registra_log("INFO", address, "Conexão", message=message)
        history = []  # Lista para armazenar o histórico do cliente
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Cliente {address[0]}:{address[1]} desconectado.")
                break

            if data == "/q":
                print(f"Cliente {address[0]}:{address[1]} solicitou desconexão.")
                registra_log("INFO", address, "solicitação", message="Solicitou desconexão")
                break
            elif data == "/l":
                print(f"Cliente {address[0]}:{address[1]} solicitou listar clientes.")
                registra_log("INFO", address, "solicitação", message="Solicitou Listar Clientes")
                response = "\n".join(f"{addr[0]}:{addr[1]}" for addr in clients.keys())
                client_socket.send(response.encode('utf-8'))
            elif data.startswith("/m:"):
                parts = data.split(":", 3)
                if len(parts) == 4:
                    _, dest_ip, dest_port, message = parts
                    dest_port = int(dest_port)
                    envia_msg(address, dest_ip, dest_port, message)
                    response = f"Mensagem enviada para {dest_ip}:{dest_port}."
                    registra_log("INFO", address, "Mensagem", message="{message} Enviada para {dest_ip}:{dest_port}")
                else:
                    response = "Comando /m inválido. Uso correto: /m:ip_destino:porta:mensagem"
                client_socket.send(response.encode('utf-8'))
            elif data.startswith("/b:"):
                message = data[3:]
                msg_geral(address, message)
                msglog=message
                response = "Mensagem enviada para todos os clientes conectados."
                registra_log("INFO", address, "Mensagem", message=f"Mensagem {msglog} Enviada para todos")
                client_socket.send(response.encode('utf-8'))
            elif data == "/h":
                response = "\n".join(history)  # Envia o histórico para o cliente
                registra_log("INFO", address, "Solicitação", message="Solicitou Historico")
                client_socket.send(response.encode('utf-8'))
            elif data == "/?":
                response = "Comandos disponíveis:\n/q - Desconectar\n/l - Listar clientes conectados\n/m:ip_destino:porta:mensagem - Enviar mensagem privada\n/b:mensagem - Enviar mensagem para todos\n/h - Ver histórico\n/? - Ajuda\n/rss:palavra_chave - Listar as 10 notícias mais recentes com a palavra-chave em RSS\n/f - Listar arquivos na pasta /server_files\n/w:url - Fazer download do arquivo da URL para a pasta /server_files\n/d:nome_arquivo - Fazer download do arquivo do servidor para o cliente"
                client_socket.send(response.encode('utf-8'))
            elif data.startswith("/rss:"):
                registra_log("INFO", address, "Mensagem", message="Solicitou Noticias")
                keyword = data[5:]
                news = noticia_rss(keyword)
                if news:
                    response = "\n".join(news)
                else:
                    response = f"Nenhuma notícia encontrada com a palavra-chave: {keyword}"
                client_socket.send(response.encode('utf-8'))
            elif data.startswith("/w:"):
                registra_log("INFO", address, "Mensagem", message="Solicitou Dowload")
                url = data[3:]
                baixar_url(url)
                response = f"Arquivo da URL {url} baixado e salvo em /server_files."
                client_socket.send(response.encode('utf-8'))
            elif data == "/f":
                registra_log("INFO", address, "Mensagem", message="Solicitou lista de arquivos do servidor")
                response = listar_arqv()
                client_socket.send(response.encode('utf-8'))
            else:
                response = "Comando inválido. Use '/q' para desconectar, '/l' para listar clientes, '/m:ip_destino:porta:mensagem' para enviar uma mensagem privada, '/b:mensagem' para enviar uma mensagem para todos, '/h' para ver o histórico, '/?' para ver os comandos disponíveis, '/rss:palavra_chave' para listar as 10 notícias mais recentes com a palavra-chave em RSS, '/f' para listar os arquivos na pasta /server_files, '/w:url' para fazer download de um arquivo da URL fornecida ou '/d:nome_arquivo' para fazer download de um arquivo do servidor para o cliente."
                client_socket.send(response.encode('utf-8'))

            # Adiciona o comando/mensagem ao histórico do cliente
            history.append(data)
    except Exception as e:
        print(f"Erro na conexão com {address[0]}:{address[1]}: {e}")
    finally:
        client_socket.close()
        del clients[address]



def envia_msg(sender_address, dest_ip, dest_port, message):
    try:
        if (dest_ip, dest_port) in clients:
            dest_socket = clients[(dest_ip, dest_port)]
            dest_socket.send(f"Mensagem de {sender_address[0]}:{sender_address[1]}: {message}".encode('utf-8'))
        else:
            raise Exception(f"Cliente {dest_ip}:{dest_port} não encontrado.")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {dest_ip}:{dest_port}: {e}")

def msg_geral(sender_address, message):
    for client_socket in clients.values():
        if client_socket != sender_address:
            client_socket.send(f"Mensagem de {sender_address[0]}:{sender_address[1]} para todos: {message}".encode('utf-8'))




"""
    Função para baixar um arquivo a partir de uma URL e salvá-lo na pasta /server_files.

    Parâmetros:
        url (str): A URL do arquivo a ser baixado.
        file_name (str): O nome do arquivo a ser salvo.

    Essa função utiliza a biblioteca requests para fazer o download do arquivo a partir da URL.
    O arquivo é baixado em pedaços e salvo na pasta /server_files com o nome especificado.
"""
def baixar_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.split("/")[-1]
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server_files", file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
        else:
            print(f"Erro ao fazer download do arquivo da URL: {url}. Código de resposta: {response.status_code}")
    except Exception as e:
        print(f"Erro ao fazer download do arquivo da URL: {url}: {e}")



"""
    Função para listar os arquivos (nome e tamanho) contidos na pasta /server_files do servidor.

    Essa função utiliza a biblioteca os para obter uma lista de arquivos na pasta /server_files.
    Para cada arquivo encontrado, a função obtém o nome e o tamanho do arquivo.
    A lista resultante contém tuplas no formato (nome do arquivo, tamanho do arquivo).
"""
def listar_arqv():
    files_list = []
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server_files")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files_list.append(f"{file_name} - {file_size} bytes")
        if files_list:
            return "\n".join(files_list)
    return "Nenhum arquivo encontrado na pasta /server_files."









