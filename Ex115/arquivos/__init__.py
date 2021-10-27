from Ex115.dados import *
def abrearquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt')
        a.write('---LISTA DE PESOAS---')
        a.close()
    except:
        print('não foi possivel criar o arquivo')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('Consultar Pessoas')
        print(a.read())


def adicionarlist(nome):
    try:
        a = open(nome, 'a')
        pessoas = {}
        Nome = str(input('Digite o nome da pessoa que você quer cadastrar: '))
        idade = leiaint('Digite a idade pessoa que você quer cadastar: ')
        pessoas['Nome'] = f'\n{Nome:<30}'
        pessoas['Idade'] = f'{idade:>5} anos'
        a.writelines(pessoas.values())
        a.close()
    except:
        print('Erro ao cadastrar pessoa')
    else:
        print(f'{Nome} Foi cadastrado com sucesso')

def fechaarquivo(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except:
        print('Erro ao fechar o arquivo')