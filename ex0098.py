from time import sleep
def contador(x, y, z):
    if z < 0:
        z = -1 * z
    if z == 0:
        z = 1
    print(f'Contagem entre {x} e {y} contando de {z} em {z}')
    if x < y:
        for c in range(x, y+1, z):
            sleep(0.3)
            print(f'{c} ', end='')
    elif y < x or z < 0:
        for c in range(x, y-1, -z):
            sleep(0.3)
            print(f'{c} ', end='')
    print()
    print('='*12, 'FIM', '='*12)


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Insira o inicio da contagem: '))
fim = int(input('Insira o termino da contagem: '))
intervalo = int(input('Insira o intervalo da contagem: '))
contador(inicio, fim, intervalo)