matriz = [[], [], []]
sumpar = sum3 = 0
for c in range(0, 3):
    for pos in range(0, 3):
        n = int(input(f'Digite o valor para  [{c}, {pos}]:  '))
        matriz[c].append(n)
print('-='*30)
for c in range(0, 3):
    for pos in range(0, 3):
        print(f'[ {matriz[c][pos]:^5} ]', end='')
    print('')
for pos, c in enumerate(matriz):
    for teta1, teta in enumerate(matriz[pos]):
        if matriz[pos][teta1] % 2 == 0:
            sumpar += matriz[pos][teta1]
        if teta1 == 2:
            sum3 += matriz[pos][teta1]
print(f'A soma dos número pares da matriz resulta em: {sumpar}')
print(f'A soma da terceira coluna da matriz resulta em: {sum3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
