#Analisando triangulos 2.0

r1 = float(input('Insira a medida da primeira reta: '))
r2 = float(input('Insira a medida da segunda reta: '))
r3 = float(input('Insira a medida da terceira reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('\033[1;32mCom os segmentos inseridos é possivel formar um triangulo ', end='')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('escaleno\033[m')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r3 == r2 and r3 != r1:
        print('isóceles\033[m')
    elif r1 == r2 and r1 == r3:
        print('equilatero\033[m')
else:
    print('\033[1;31mCom os segmentos inseridos NÃO é possivel formar um triângulo\033[m')