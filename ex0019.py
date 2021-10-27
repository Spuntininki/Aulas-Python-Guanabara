#Um professor quer quer sorter um de seus quatro alunos para apagar o quadro. crie um programa que leio o nome de cada aluno
# e escreva o nome de um dos alunos
from random import choice
a = str(input('Insira o nome do primeiro aluno: '))
b = str(input('Insira o nome do segundo aluno: '))
c = str(input('Insira o nome do terceiro aluno: '))
d = str(input('Insira o nome do quarto aluno: '))
lista = [a, b, c, d]
print('o aluno sorteado é {}'.format(choice(lista)))


