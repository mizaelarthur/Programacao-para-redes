# Funções de armazenamento de LOG
import datetime

LOG_FILE = "server_log.txt" # Especificando nome do arquivo


"""
    Função para escrever registros de log em um arquivo.

    Parâmetros:
        action_type (str): Tipo de ação (INFO, WARNING, etc.).
        address (tuple): Endereço IP e porta de origem.
        command (str): O comando recebido.
        message (str, opcional): A mensagem associada ao comando (se aplicável).
        dest_address (tuple, opcional): Endereço IP e porta de destino (para comandos /m e /b).

    Essa função registra informações relevantes no arquivo de log para cada ação realizada pelo servidor.
    Cada linha do arquivo de log contém:
    - Data e hora em que a ação ocorreu
    - Tipo de ação (INFO, WARNING, etc.)
    - Endereço IP e porta de origem
    - O comando recebido
    - (Opcional) Endereço IP e porta de destino (para comandos /m e /b)
    - (Opcional) A mensagem associada ao comando
"""
def registra_log(action_type, address, command, message=None, dest_address=None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_entry = f"{now} | {action_type} | {address[0]}:{address[1]} | {command}"
        if action_type == "Mensagem":
            log_entry += f" | {dest_address[0]}:{dest_address[1]}"
        if message:
            log_entry += f" | {message}"
        log_file.write(log_entry + "\n")
