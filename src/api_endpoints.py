import requests

base_url = "https://dragonball-api.com/api"

# Criar as funcoes que irao pegar os dados da api
# nome da funcao deve ter o prefixo get, post ou put

def get_planetas():
    # 1 - Definir o endpoint que vai ser consumido
    url = f"{base_url}/planets"

    # 2 - Fazer a requisição (pedindo os dados)
    dados = requests.get(url)

    # 3 - Retornar os dados
    return dados.json()

def get_personagens():
    url = f"{base_url}/characters"
    dados1 = requests.get(url)
    return dados1.json()

print(get_personagens())

# TODO: Fazer a requisição para pegar a lista de personagens
