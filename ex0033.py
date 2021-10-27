#escreva um programa que leia tres numeros e mostre na tela qual é o maior e qual é o menor
n1 = int(input('Qual o primeiro numero? '))
n2 = int(input('Qual o segundo numero? '))
n3 = int(input('Qual o terceiro numero? '))

if n1 > n2 and n1 > n3:
    print('O maior numero é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior numero é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior numero é {}'.format(n3))

menor = n1

if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n2

print('O menor número é {}'.format(menor))