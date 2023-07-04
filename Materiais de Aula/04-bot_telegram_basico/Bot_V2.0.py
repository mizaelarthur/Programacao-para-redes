import requests

API_Key= '6378409306:AAGR6mxdCDqNiWOiRzRvS6FBxE2zdP8gU94'
url_req = f'https://api.telegram.org/bot{API_Key}'

requisicao = requests.get(url_req+'/getUpdates')

print(requisicao.status_code)

retorno = requisicao.json()

id_chat = retorno['result'][0]['message']['chat']['id']

mensagem= input('Digite a Mensagem: ')

resposta = {'chat_id':id_chat,'text':mensagem}

envio = requests.post(url_req+'/sendMessage',data=resposta)

