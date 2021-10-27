#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
#calcule o preço a pagar, sabendo que custa R$60,00 por dia e R$0,15 por Km rodado.

d = int(input('insira a quantidade de dias: '))
k = float(input('insira a kilometragem rodada: '))
print('o valor do aluguel do carro vai custar: {:.2f}'.format((60.00*d)+(0.15*k)))
