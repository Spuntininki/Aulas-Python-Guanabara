lista = ('Pão', 2.00, 'Leite', 3.50, 'Miojo', 1.50, 'Suco', 3.00, 'Bicicleta', 500.00)
print('-'*50)
print(f'\033[1;34m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('-'*50)
for cont, c in enumerate(lista):
    if cont % 2 == 0:
        print(f'{c:.<30}', end='')
    else:
        print(f'R$ {c:>7.2f}')
print('-'*50)