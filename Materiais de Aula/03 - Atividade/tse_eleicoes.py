# Solicitar Ano
# Solicitar a sigla do estado
# Solicitar Cargo
# Solicitar o ID da eleição(Exemplo: 544 ou 546)
'''
    O TSE divulga na sua página oficial um webservice que fornece os dados 
    das apurações das eleições realizadas no Brasil.

    O fragmento de código a seguir monta um dicionário (dados_retorno) com o 
    resultado das eleições do ano de 2022 no 1º turno para Presidente.

    Com base na documentação da API contida na URL 
    https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022


    Pede-se que seja desenvolvido um programa que solicite ao usuário o 
    ano da eleição, tipo de eleição (estadual, nacional) e o cargo eletivo 
    e o programa  deverá montar um dicionário {k:v} no seguinte formato:
    {
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        ...
    }
    
    O dicionário deverá ser ordenado de forma decrescente pela quantidade de
    votos que o candidato obteve.

    Em seguida, deverá ser gerado um arquivo (resultados.txt) onde na 
    primeira linha deverá constar a seguinte string:
        numero;nome,partido;quantidade_votos;percentual_votos

    Da segunda linha em diante deverão constar os dados correspondentes de
    cada candidato
'''

import requests

url = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'

# Primeiramente vamos perguntar

# Vamos solicitar os dados e armazenar em uma variável
dados_retorno = requests.get(url).json()

# Vamos criar uma váriavel para nosso arquivo.txt
arquivo = open('resultados.txt', 'w')

# Em seguida vamos guardar as informações no nosso arquivo criado
#arquivo.write(Variavel Final)
print(dados_retorno)

# Agora fazemos um print só para informar que o arquivo foi gerado
print('Arquivo gerado com sucesso!')
