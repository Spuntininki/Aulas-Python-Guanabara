#Faça um programa que leia um numero de 0 a 9999e mostre na tela cada um dos digitos separados.

n = int(input('Insira um numero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unindade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)
'''print('Unidade: {}'.format(n[0][3]))
print('dezena: {}'.format(n[0][2]))
print('centena: {}'.format(n[0][1]))
print('milhar: {}'.format(n[0][0]))'''



