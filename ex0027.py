#Faça um programa que leia o nome de uma pessoa e mostre o primeiro e o ultimo nome.

nome = str(input('Insira o seu nome completo: '))
nome = nome.split()
'''sobre = nome[-1::]
print('O seu primeiro nome é: {} e seu ultimo nome é: {}'.format(nome[0], sobre[0]))'''
#Solução GUANABARA
print('Seu primeiro nome é: {} e seu sobrenome é: {}'.format(nome[0], nome[len(nome)-1]))
print(len(nome))