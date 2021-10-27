#Faça um programa que leia tres comprimentos e diga se essas linhas podem ou nãp formar um triangulo
print('-=-' * 20)
print('ANALISANDO TRIANGULOS')
print('-=-' * 20)
r1 = float(input('Insira o o primeiro segmento: '))
r2 = float(input('Insira o segundo segmento: '))
r3 = float(input('Insira o terceiro segmento: '))

'''if r1 > r2 and r1 > r3:
    maior = r1
    soma = r2 + r3
if r2 > r1 and r2 > r3:
    maior = r2
    soma = r1+r3
if r3 > r1 and r3 > r2:
    maior = r3
    soma = r2+r1

if maior < soma:
    print('Com as medidas inseridas é possivel fazer um triangulo: ')
else:
    print('Com as medidas inseridas NÃO é possivel fazer um triangulo: ', maior, soma)'''
#Solução GUANABARA

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2 +r3:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima NÃO podem formar um triangulo')