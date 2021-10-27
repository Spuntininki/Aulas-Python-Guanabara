#Progressão aritimetica

n = int(input('Insira o primeiro termo da progressão aritimetica: '))
r = int(input('Insira a razão da progressão: '))
soma = n + r
print('\033[1;32mSegue a Progressão aritimetica:\033[m')
print('({}'.format(n), end=',')
for c in range(1, 10):
    if c == 9:
        print('{}'.format(soma), end='...)')
    else:
        print('{}'.format(soma), end=',')
    soma = soma + r
