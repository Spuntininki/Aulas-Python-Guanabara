#Faça um programa que mostre a soma entre todos os numeros impares que são multiplos de 3 entre 1 a 500

soma = 0
num = 0
for c in range(1, 500+1, 2):
    if  c % 3 == 0:
        print(c, end=' ')
        num += 1
        soma = soma + c
print( )
print('A soma dos {} numeros resulta em {}'.format(num, soma))