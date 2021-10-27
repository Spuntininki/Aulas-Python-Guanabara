#Crie um programa que leia a data de nascimento de 7 pessoas e mostre quantas delas já atigniram a maioridade.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    data = int(input('Insira o Ano da de nascimento da {} pessoa: '.format(c)))
    if atual - data > 18:
        maior += 1
    else:
        menor += 1

print('Um total de {} pessoas já atingiram a maioridade e um total de {} pessoas são menores'.format(maior, menor))
