#Progressão aritimetica 2.0

n1 = int(input('Digite o primeiro termo da progressão: '))
raz = int(input('Digite a razão da PA: '))
soma = n1 + raz
print('{}'.format(n1), end=' ')
c = 1
d = 10
decision = ''
while c != d:
    print('{}'.format(soma), end=' ')
    soma = soma + raz
    c += 1
    if c == d:
        print('')
        n1 = int(input('Insira quantos termos gostaria de ver a mais: '))
        d = d + n1
print('Obrigado pela preferencia!')





'''if c == d:
print(' ')
decision = str(input('Deseja continuar? Y/N ')).upper()
if decision == 'Y':
n1 = int(input('Digite Quantos termos gostaria de ver a mais: '))
d = d + n1
if n1 == 0:
    c = d
elif decision == 'N':
print('Obrigado pela preferencia.')
else:
print('\033[1;31mOpção invalida, o programa irá se encerrar.\033[m')'''