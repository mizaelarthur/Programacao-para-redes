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



if __name__ == "__main__":
    clients = {}

    # Criar arquivo de log
    open(LOG_FILE, "w").close()

    start_server()


















clients = {}

