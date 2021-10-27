#Cria um prorama que lei o quanto a pessoa tem em real na carteira e mostre quantos dolares ela pode comprar
#considerando dolar 5,18
r = float(input('Insira o valor em real que possui: R$'))
d = r/5.18

print('com tantos R${:.2f} você consegue comprar US${:.2f} dolares'.format(r, d))