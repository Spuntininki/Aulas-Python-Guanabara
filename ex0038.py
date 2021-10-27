# escreva um programa que leia dois numeros inteiros e mostre qual é o maior e qual é o menor ou mostre se os dois são
# iguais.

n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))

if n1 > n2:
    print('o maior número é {} e o menor número é {}'.format(n1, n2))
elif n2 > n1:
    print('o maior número é {} e o menor número é {}'.format(n2, n1))
else:
    print('{}Não existe numero maior os dois são iguais{}'.format('\033[1;33m','\033[m'))