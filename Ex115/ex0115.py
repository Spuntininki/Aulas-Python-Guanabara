from Ex115.dados import *
from Ex115.arquivos import *
from time import sleep
arquivo = 'Dados_cadastrais.txt'
if not abrearquivo(arquivo):
    criararquivo(arquivo)
    print('Arquivo criado com sucesso')
while True:
    titulo('MENU PRINCIPAL')
    resposta = menu(['Cadastrar pessoas', 'Consultar pessoas', 'Sair do programa'])
    if resposta == 1:
        titulo('Cadastrar pessoas')
        adicionarlist(arquivo)
        break
    elif resposta == 2:
        lerarquivo(arquivo)
        break
    elif resposta == 3:
        linha()
        print('Saindo do sistema...')
        fechaarquivo(arquivo)
        linha()
        break
    else:
        print('\033[1;31mOpção invalida.\033[m')
        break
sleep(1)
print('Até a proxima!')
