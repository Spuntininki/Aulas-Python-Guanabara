# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da Casa?'))
salario = float(input('Insira o salário do comprador: '))
anos = int(input('Em Quantos anos pretende pagar?'))
prestaçao = casa / (anos*12)
if prestaçao > (salario * 30) / 100:
    print('\033[1;31mEMPRESTIMO NEGADO\033[m')
    print('O valor da prestação de R${:.2f} excede 30% do salario do comprador por isso não será possivel o emprestimo.'.format(prestaçao))
else:
    print('\033[1;32mEMPRESTIMO APROVADO\033[m')
    print('O emprestimo do imóvel cujo o valor é R${:.2f} '.format(casa), end='')
    print('foi aprovado, tendo uma prestação de R${:.2f}'.format(prestaçao))