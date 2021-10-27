n = int(input('Digite um Numero qualquer: '))
d = n % 2

if d == 0:
    print('O numero {}{} é par{}'.format('\033[1;32m', n, '\033[m'))
else:
    print('O numero {}{} é impar{}'.format('\033[1;31m', n, '\033[1;31m'))

