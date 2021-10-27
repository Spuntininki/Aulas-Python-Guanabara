from ex0111.utilidadecursoemvideo import moeda


n = float(input('Digite o valor: R$ '))
aum = int(input('Insira o percentual de aumento desejado: '))
dim = int(input('Insira o percentual de redução desejado:'))
print(f'O valor {moeda.fmoeda(n)} com um aumento de {aum}% resulta em {moeda.fmoeda(moeda.aumentar(n, aum))}')
print(f'O valor {moeda.fmoeda(n)} com a diminuição de {dim}% resulta em {moeda.fmoeda(moeda.diminuir(n, dim))}')
print(f'O dobro de {moeda.fmoeda(n)} é {moeda.fmoeda(moeda.dobro(n))}')