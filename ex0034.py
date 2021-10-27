sal = float(input('Qual o salário do funcionario?'))
if sal >= 1250.00:
    print('O salário terá um aumento de R${:.2f} resultando no total de R${:.2f}'.format(sal*0.10, sal*1.10))
else:
    print('O salário terá um aumento de R${:.2f} resultando no total de R${:.2f}'.format(sal*0.15, sal*1.15))
