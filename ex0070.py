condition = prodbarato = ''
totalgasto = prodacima = contbarato = 0
c = 1
print('\033[1;33m-'*30)
print('MERCADÃO GOSTOSÃO')
print('-'*30, '\033[m')
while True:
    nome = str(input('Insira o nome do produto: '))
    preço = float(input('Preço R$ '))
    totalgasto += preço
    if preço >= 1000:
        prodacima +=1
    if c == 1:
        contbarato = preço
        prodbarato = nome
    if preço < contbarato:
        contbarato = preço
        prodbarato = nome
    while True:
        condition = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if condition in 'S':
            print('-'*30)
            break
        elif condition in 'N':
            print('Obrigado pela preferencia volte sempre!')
            break
        else:
            print('Opção incorreta, tente novamente')
    c += 1
    if condition in 'Nn':
        break
print(f'O total da compra irá deu em {totalgasto:.2f}')
print(f'essa compra possui um total de {prodacima} produtos acima de R$1000,00')
print(f'o produto mais barato foi o {prodbarato}')
