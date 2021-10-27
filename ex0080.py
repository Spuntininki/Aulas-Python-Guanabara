lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Valor adicionado como ultimo da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Valor adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-='*30)
print(f'Os valores em ordem crescente ficou {lista}')
