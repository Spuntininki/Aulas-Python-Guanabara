lista = []
opcao = ''
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('\033[1;32mValor Adicionado com sucesso!\033[m')
    else:
        print('\033[1;31mNúmero repetido! não será adicionado..\033[m')
    while True:
        opcao = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
        if opcao in 's':
            break
        elif opcao in 'n':
            break
    if opcao in 'n':
        break
lista.sort()
print(f'Você digitou {lista}')
