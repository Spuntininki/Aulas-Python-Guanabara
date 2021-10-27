tup1 = (int(input('Digite o 1° número: ')), int(input('Digite o 2° número: ')),
        int(input('Digite o 3° número: ')) , int(input('Digite o 4° número: ')))
print(f'O número 9 foi digitado {tup1.count(9)} vezes')
if 3 in tup1:
    print(f'O número três foi digitado na primeira vez na {tup1.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for c in tup1:
    if c % 2 == 0:
        print(f'{c}', end=' ')
