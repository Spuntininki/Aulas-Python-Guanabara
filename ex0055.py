maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('Insira o peso da {}° pessoa: '.format(c)))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peo lido foi {:.1f}KG'.format(maior))
print('O menor peso lido foi {:.1f}KG'.format(menor))

