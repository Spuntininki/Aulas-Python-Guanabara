print('\033[1;33m-=-' * 20)
print('TABUADA 2.0')
print('-=-' * 20, '\033[m')

'''for c in range(1, 10+1):
    if c == c:
        print('\033[1;33mTABUADA DO {}\033[m'.format(c))
        print(' ')
    for i in range(1, 10+1):
        print('{} X {} = {}'.format(i, c, i*c))'''

n = int(input('Digite o Numero que você gostaria de ver a tabuada: '))
print('\033[1;34mTABAUDA DO {}\033[m'.format(n))
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, n*c))