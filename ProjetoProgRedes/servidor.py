'''Realizando a importação de bibliotecas Python
   para nos ajudar com as demandas '''

import socket
import threading
import feedparser
import requests
import os

# Agora vamos importas os outros arquivos de Configuração
from comunicação_cliente import  *
from log import LOG_FILE


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Cliente {address[0]}:{address[1]} conectado.")
        clients[address] = client_socket
        client_handler = threading.Thread(target=comandos, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    clients = {}

    # Criar arquivo de log
    open(LOG_FILE, "w").close()

    start_server()


















clients = {}

