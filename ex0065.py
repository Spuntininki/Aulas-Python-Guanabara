choice = ''
maior = menor = c1 = c = n = media = divisor = 0
count = 1
while c == 0:
    n = int(input('Digite um número: '))
    c1 = 0
    media += n
    divisor += 1
    if divisor == 1:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    while c1 == 0:
        choice = str(input('Deseja continuar Y/N?')).upper().strip()[0]
        if choice == 'Y':
            c = 0
            c1 = 1
        elif choice == 'N':
            c = 1
            media = media / divisor
            c1 = 1
        else:
            print('\033[1;31mNão consegui te entender tente novamente\033[m')
            c1 = 0

print('A média dos número digitados resulta em {} '
      '\no maior valor foi {} e o menor valor foi {}'.format(media, maior, menor))