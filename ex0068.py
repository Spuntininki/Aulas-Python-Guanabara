#JOGO DE PAR OU IMPAR
from random import randint
c = randint(1, 10)
soma = n = contador = 0
escolha = ''
while True:
    n = int(input('Digite um valor: '))
    escolha = str(input('Impar ou Par, qual sua escolha? ')).strip()[0]
    soma = c + n
    if escolha in 'Pp':
        if soma % 2 != 0:
            print(f'A soma resultou em {soma} e é um número ímpar.')
            print('\033[1;31mPERDEU\033[m')
            print(f'Você venceu {contador} vezes')
            break
        else:
            print(f'A soma resultou em {soma} e é um número par')
            print('\033[1;32mVenceu\033[m')
            print('-'*30)
            contador += 1
            soma = 0
    elif escolha in 'Ii':
        if soma % 2 == 0:
            print(f'A soma resultou em {soma}e é um número PAR')
            print('\033[1;31mPERDEU\033[m')
            print(f'Você venceu {contador} vezes')
            break
        else:
            print(f'A soma resultou em {soma} e é um número IMPAR')
            print('\033[1;32mVENCEU\033[m')
            print('-' * 30)
            contador += 1
            soma = 0
    else:
        print('\033[1;31mopção invalida\033[m')
