#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
ca = float(input('Insira o valor do cateto adjacente: '))
co = float(input('Insira o valor do cateto oposto:  '))
'''soma = ca**2+co**2
print('O valor do cateto adjacente é {} e do oposto {}, assim o valor da hipotenusa é {}'.format(ca, co, math.sqrt(soma)))'''

hi = math.hypot(ca, co)

print('O valor do cateto adjacente é {} e do oposto {}, assim o valor da hipotenusa é {:.2f}'.format(ca, co, hi))

