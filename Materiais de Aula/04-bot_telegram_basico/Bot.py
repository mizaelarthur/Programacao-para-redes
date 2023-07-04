import requests

API_Key= '6378409306:AAGR6mxdCDqNiWOiRzRvS6FBxE2zdP8gU94'
url_req = f'https://api.telegram.org/bot{API_Key}'

requisicao = requests.get(url_req+'/getUpdates')

print(requisicao.status_code)
print(requisicao.json())

id_chat = int(input('Informe o ID do Chat: '))
resposta = {'chat_id':id_chat,'text':'Olá...'}
envio = requests.post(url_req+'/sendMessage',data=resposta)

