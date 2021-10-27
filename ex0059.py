#Calculadora simples
from time import sleep

escolha = ''
c = 1
opção = False
d = ''
while c > 0:

    sleep(1)
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    while not opção:
        print('''ESCOLHA UMA DAS OPÇÕES:
        [1] para SOMAR
        [2] para SUBTRAIR
        [3] PARA MULTIPLICAR
        [4] PARA DIVIDIR
        [5] SAIR DO PROGRAMA''')
        i = int(input('qual a sua escolha? '))
        if i == 1:
            print('A soma entre {} e {} resulta em {}'.format(n1, n2, n1+n2))
        elif i == 2:
            print('A subtração entre {} e {} resulta em {} '.format(n1, n2, n1-n2))
        elif i == 3:
            print('A multiplicação entre {} e {} resulta em {}'.format(n1, n2, n1*n2))
        elif i == 4:
            print('A divisão entre {} e {} resulta em {}'.format(n1, n2, n1/n2))
        elif i == 5:
            c = 0
        else:
            print('\033[1;31mOPÇÃO INVALIDA\033, TENTE NOVAMENTE...\033[m')

        d = str(input('Deseja usar os mesmos valores? SIM/NÃO ')).upper().strip()[0]
        if d == 'N':
            opção = True
        elif d == 'S':
            opção = False
        else:
            d = str(input('Opção invalida tente novamente: '))