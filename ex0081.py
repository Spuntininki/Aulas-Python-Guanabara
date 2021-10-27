lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        opcao = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
        if opcao in 's':
            break
        elif opcao in 'n':
            break
    if opcao in 'n':
        break
print(f'Foi digitado {len(lista)} elementos.')
if 5 in lista:
    print(f'O número 5 se encontra na lista, o primeiro cinco se encontra na posição {lista.index(5)}')
else:
    print('O número 5 não se encontra na lista.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é: {lista}')
