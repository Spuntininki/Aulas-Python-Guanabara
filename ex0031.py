#Desenvolva um programa que pergunte a distancia de uma viagem em Km, calcule o preço da passagem, cobrando R$ 0,50 por
#por Km e para viagens acima de 200Km cobre R$0,45
k = float(input('qual a distancia da viagem em Km?'))

if k <= 200:
    print('O valor da passagem é de R${:.2f}'.format(k*0.50))
else:
    print('O valor da passagem é de  R${:.2f}'.format(k*0.45))

##maneira alternativa para criar a condicional: preço = k *0.50 if k<= 200 else k * 0.45