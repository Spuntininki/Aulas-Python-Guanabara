#Programa que lê um numero inteiro positivo qualquer e mostra seu fatorial
from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {} '.format(n, f))
'''c = n
fator1 = n
resultado = n * (n-1)
for c in range(1, n-1):
    n -= 1
    resultado = resultado * (n-1)

print('O fatorial de {} resulta em {}'.format(fator1, resultado))'''
'''while c != 1:
    n = n * (c-1)
    c -= 1
print('O fatorial de {} resulta em {}'.format(fator1, n))'''

