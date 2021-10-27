#escreva um programa que leia o salario de um funcionario e mostre ele com 15% de aumento

n = float(input('Insira o salario do funcionario: '))

print('o salario de {} agora com um aumento de 15% vale: {:.2f}'.format(n, n*1.15))

#ou n + (n*15/100)