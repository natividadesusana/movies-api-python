import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?apikey=e9409fce&t=' + titulo + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão!!')
        return None

def print_detalhes(filme):
    print('\nTitulo Filme: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Atores: ', filme['Actors'])
    print('Diretores: ', filme['Director'])
    print('Nota: ', filme['imdbRating'])
    print('Prêmios: ', filme['Awards'])
    print('Poster: ', filme['Poster'])
    print('')

sair = False
while not sair:
    print('\nBem-Vindo!')
    opcao = input('\n~ Escreva o nome de um Filme ou SAIR para fechar: ')

    if opcao == 'SAIR':
        sair = True
        print('\nAté Logo!')
    else:
        filme = requisicao(opcao)
        if filme['Response'] == 'False':
            print('\nFilme não encontrado!!')
            print('--------------------------')
        else:
            print_detalhes(filme)