contM = contF = contI = 0
decisão = ''

while True:
    idade = int(input('Insira a Idade: '))
    sexo = str(input('Insira o sexo [F/M]: ')).strip()[0]
    if idade > 18:
        contI += 1
    if sexo in 'Mm':
        contM += 1
    if sexo in 'Ff' and idade < 20:
        contF += 1
    while True:
        decisão = str(input('Deseja continuar? [S/N] ')).strip()[0]
        if decisão in 'Nn':
            print(f'no grupo inserido possui um total de {contI} pessoa(s) acima de 18 anos')
            print(f'Possui um total de {contM} homen(s) cadastrado(s)')
            print(f'e Posui um total de {contF} mulher(es) abaixo de 20 anos cadastrada(s)')
            print('Obrigado pela preferencia!')
            break
        elif decisão in 'Ss':
            print('-'*30)
            break
        else:
            print('Opção incorreta!')
    if decisão in 'Nn':
        break




