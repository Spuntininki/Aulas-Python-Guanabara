from ex0111 import moeda


n = float(input('Digite o valor: R$'))
print(f'O dobro de {moeda.fmoeda(n)} resulta em {moeda.dobro(n, True)}')
print(f'A metade de {moeda.fmoeda(n)} resulta em {moeda.metade(n, True)}')
print(f'O aumento de 10%  resulta em {moeda.aumentar(n, 10, True)}')