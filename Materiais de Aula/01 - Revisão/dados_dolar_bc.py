# Primeiramente vamos instalar uma biblioteca para nos auxiliar
import requests

url  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-2021%27&@dataFinalCotacao=%2712-31-2021%27&$format=json'

# Vamos coletar agora os dados referentes a URL
#dados = requests.get(url)

# Vamos exibir nossa resposta
#print(dados)

# O Retorno é feito em lista, e cada elemento da lista é um dicionário, para isso, vamos colocar um json para leitura

dados = requests.get(url).json()

# Vamos exibir a leitura da lista como um todo
print(dados['value'])

# Vamos exibir agora somente o primeiro item da lista dados
#print(dados[0])

# Agora vamos listar quantos elementos temos na lista

