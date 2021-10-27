#Exercício Python 37: Escreva um programa em Python
# que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um Numero inteiro qualquer: '))
numconv = str(0)
conv = 0
while n//2 > 0:
    conv = str(n % 2)
    numconv = str(numconv+ conv)
    n = n // 2
print(numconv)
'while n // 2 > 0:'
'''print('\033[1;33mEscolha a opção de conversão')
print('[1] - para binário')
print('[2] - para octal')
print('[3] para hexadecimal\033[m')
choice = int(input('Então qual é a sua escolha? '))
if choice == 1:
    print('{} convertido para binário resulta em {}'.format(n, bin(n)[2:]))
elif choice == 2:
    print('{} convertido para octal resulta em {}'.format(n, oct(n)[2:]))
elif choice == 3:
    print('{} convertido para hexadecimal resulta em {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!!')'''