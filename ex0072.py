#número por extenso entre 0 e 20
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
decisão = 0
while True:
    while decisão == 0:
        n = int(input('Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            decisão = 1
            print(f'Você digitou o número {numeros[n]}')
        else:
            print('Tente Novamente.', end='')
    decisão = str(input('Deseja continuar? [Y/N]')).strip().upper()[0]
    if decisão in 'Y':
        decisão = 0
    elif decisão in 'N':
        break
    else:
        print('TENTE NOVAMENTE.', end=' ')


