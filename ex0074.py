##SOLUÇÃO ALTERNATIVA
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('\033[1;32mOS NÚMEROS SORTEADOS FORAM: \033[m')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior número sorteado foi {max(n)}')
print(f'O menor número sorteado fo {min(n)}')



'''from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
tup1 = (n1, n2, n3, n4, n5)
maior = 0
menor = 0
print('Os Números sorteados foram: ', end=' ')
for cont, c in enumerate(tup1):
    if cont == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    print(f'{c}', end=' ')
print('')
print(f'O maior número foi {maior} e o menor número foi {menor}')'''
