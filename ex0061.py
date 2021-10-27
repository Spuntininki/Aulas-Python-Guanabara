#Progressão aritimetica com WHILE
n1 = int(input('Insira o primeiro termo da progressão aritmetica: '))
raz = int(input('Insira a razão da PA: '))
soma = n1 + raz
c = 1
print('({}'.format(n1), end=',')
while c != 10:
    if c == 9:
        print('{}'.format(soma), end=')')
        c += 1
    else:
        print('{}'.format(soma), end=',')
        soma = soma + raz
        c += 1
