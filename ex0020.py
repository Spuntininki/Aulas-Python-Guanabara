from random import shuffle
n1 = str(input('Insira o Nome do primeiro aluno: '))
n2 = str(input('Insira o Nome do segundo aluno: '))
n3 = str(input('Insira o Nome do terceiro aluno:'))
n4 = str(input('Insira o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
