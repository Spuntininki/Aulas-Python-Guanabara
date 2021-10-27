from ex0111.utilidadecursoemvideo import moeda

n = float(input(f'insira o valor: '))
aum = int(input('Defina o percentual de aumento desejado: '))
dim = int(input('Defina o percentual de redução desejado: '))
print(f'O valor com o aumento de 10% resulta em R${moeda.aumentar(n, aum):.2f}')
print(f'O valor com uma redução de 10% resulta em R${moeda.diminuir(n, dim):.2f}')
print(f'O valor inserido sendo dobrado resulta em R${moeda.dobro(n):.2f}')
print(f'A metade do valor inserido resulta em R${moeda.metade(n):.2f}')

