#faça um algoritimo que leia o preço de um produto e mostre ele com 5% de desconto

n = float(input('insira o valor do produto a ser dado o desconto: '))

print('o produto com 5% de desconto agora vale: {:.2f}'.format(n*0.95))


#ou n - (n*5/100)