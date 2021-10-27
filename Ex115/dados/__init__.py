from time import sleep


def linha():
    print('-' * 42)


def titulo(frase):
    linha()
    print(f'{frase}'.center(42))
    linha()


def menu(lista=[]):
    t = 1
    for c in lista:
        print(f'\033[1;32m{t} -\033[m \033[1;34m{c}\033[m')
        t += 1
    linha()
    opcao = leiaint('Sua opção: ')
    return opcao



def leiaint(frase):
    while True:
        try:
            n = str(input(frase))
            if n != '':
                return int(n)
            else:
                n = 0
                print('\033[1;31mO usuário resolveu não digitar esse número.\033[m')
                return n
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, Digite um número valido.\033[m')





