#Numero primo?
n = int(input('Insira Um Numero: '))

soma = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;32m', end='')
        soma = soma + 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
if soma == 2:
    print('\033[m')
    print('\033[1;32mO numero {} é primo!\033[m'.format(n))
else:
    print('\033[m')
    print('\033[1;33mO numero {} NÃO é primo\033[m'.format(n))