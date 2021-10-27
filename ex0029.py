vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    vel = vel - 80
    print('\033[1;31mVOCE FOI MULTADO!!!\033[m')
    print('\033[1;31mO valor da multa é de R${:.2f}\033[m'.format(vel*7.00))
else:
    print('\033[1;32mVocê está dentro da velocidade permitida!\033[m')