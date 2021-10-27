from random import randint
from  time import sleep



def sorteia(a):
    for c in range(0, 5):
        a.append(randint(0, 10))
    print('sorteando 5 valores na lista:', end='')
    for c in a:
        print(f'{c} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar(a):
    pares = 0
    for c in a:
        if c % 2 == 0:
            pares += c
    print(f'Somando os números pares de {a}, temos {pares}')


lista = []
sorteia(lista)
somapar(lista)
