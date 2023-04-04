# Primeiramente vamos instalar uma biblioteca para nos auxiliar
import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

# Vamos coletar agora os dados referentes a URL
dados = requests.get(url)

# Vamos exibir nossa resposta
print(dados)

# O Retorno é feito em lista, e cada elemento da lista é um dicionário, para isso, vamos colocar um json para leitura

dados = requests.get(url).json()

# Vamos exibir a leitura da lista como um todo
print(dados)

# Vamos exibir agora somente o primeiro item da lista dados
print(dados[0])

print(100*=)

# Agora vamos listar quantos elementos temos na lista
