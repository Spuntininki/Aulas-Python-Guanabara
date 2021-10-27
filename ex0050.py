#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma daqueles apenas que forem pares se o valor digitado
#for impar desconsidere-o
soma = 0
sumim = 0
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma = soma + n
    else:
        sumim = sumim + n

print('A soma dos numeros pares resultou em: {} e a soma dos numeros impares resultou em {}'.format(soma, sumim))
