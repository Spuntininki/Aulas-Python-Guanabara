#Elabore um programa que calcule o valor a ser pago por
#um produto, considerando o seu preço normal e condição de pagamento

print('\033[1;32m{:=^40}\033[m'.format(' LOJAS FONSECA '))

pre = float(input('Insira o preço do produto:'))
print('\033[1;34mDependendo da forma de pagamento terá uma alteração no valor do produto!')
print('Suas opções são:')
print('1- À vista DINHEIRO/CHEQUE: 10% de desconto')
print('2- À vista no CARTÃO: 5% de desconto')
print('3- em até 2x NO CARTÃO: preço normal')
print('4- 3x OU MAIS no cartão: 20% de juros\033[m')
pag = int(input('Digite o numero correspondente da forma de pagamento desejada( 1, 2, 3, 4): '))
if pag == 1:
    pre = pre - (pre*0.10)
elif pag == 2:
    pre = pre - (pre*0.05)
elif pag == 3:
    pre = pre
    print('A sua compra irá sair por 2x de R${:.2f}'.format(pre/2))
elif pag == 4:
    pre = pre*1.20
    parc = int(input('Quantas vezes?'))
    print('A sua compra irá sair por 10x de R${:.2f}'.format(pre/parc))
else:
    pre = 0
    print('\033[1;31mOPÇÃO INVALIDA\033[m')
print('O valor do produto com essa forma de pagamento será de {:.2f}'.format(pre))