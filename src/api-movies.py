import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?apikey=e9409fce&t=Divergent')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão!!')
        return None

def print_detalhes(filme):
    print('Titulo Filme: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Atores: ', filme['Actors'])
    print('Diretores: ', filme['Director'])
    print('Nota: ', filme['imdbRating'])

sair = False
while not sair:
    opcao = input('Escreva o nome de um Filme ou SAIR para fechar: ').upper

    if opcao == 'SAIR':
        sair = True
    else:
        filme = requisicao(opcao)