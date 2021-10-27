def area(x, y):
    a = x * y
    print(f'a aréa de um terreno {x}x{y} é {a}m²')

print('Controle de Terrenos')
print('-'*30)
l = float(input('Insira a largura do terreno (m): '))
c = float(input('Insira o comprimento do terreno (m): '))
area(l, c)