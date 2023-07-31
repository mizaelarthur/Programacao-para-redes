# Aqui vamos colocar as funções de comunicação com o BOT TELEGRAM
# Vamos importar os outros códigos
import requests
import servidor


# Telegram COnfigurações
chave_api = "<chave-aqui>"
id_chat = 00000000 #Troque pelo número do seu chat





#=================================================================
"""
    Função para enviar mensagem para o bot Telegram usando a API do Telegram.

    Parâmetros:
        message (str): A mensagem a ser enviada.

    Essa função utiliza a API do Telegram para enviar uma mensagem para o bot.
    Ela faz uma solicitação HTTP POST para a URL da API do Telegram com os dados da mensagem.
    A mensagem é enviada para o chat associado ao chat_id especificado na variável CHAT_ID.
"""
def envia_msg_telegram(message):
    url = f"https://api.telegram.org/bot{chave_api}/sendMessage"
    data = {
        "chat_id": f"{id_chat}", 
        "text": message,
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")
