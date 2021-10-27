lista1 = []
while True:
    lista1.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
        if opcao in 's':
            break
        elif opcao in 'n':
            break
    if opcao in 'n':
        break
print('-='*30)
print(f'A lista complenta é {lista1}')
listapar = []
listaimpar = []
for c in lista1:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista par é {listapar}')
print(f'A lista impar é {listaimpar}')
