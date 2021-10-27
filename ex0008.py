#escreva um programa que leia um valor em metros e o exiba conertido em milimetros e centimetros

a = int(input('insira o valor em metros'))
decim = a*10
cent = a*100
milim = a*1000

print('a quantidade {} convertida em centimetros é {}, em milimetros é {}, e em decimetros {} '.format(a, cent, milim, decim))
