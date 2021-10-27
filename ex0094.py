dados = []
div = 0
totidade = 0
while True:
    dados.append({})
    dados[div]['nome'] = str(input('Digite o nome: '))
    while True:
        sexo = str(input('Masculino ou feminino? [M/F]')).strip().upper()[0]
        if sexo in 'MF':
            dados[div]['sexo'] = sexo
            break
        else:
            print('Por favor insira apenas "M" ou "F", tente novamente.')
    dados[div]['idade'] = int(input('Insira a idade: '))
    totidade += dados[div]['idade']
    div += 1
    while True:
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if opcao in 'S':
            break
        elif opcao in 'N':
            break
        else:
            print('Opção invalida, tente novamente')
    if opcao in 'N':
        break
media = totidade/div
print('-'*30)
print(f'no total foram cadastradas {len(dados)} pessoas')
print(f'A media da idade do grupo é de {totidade/div}')
print('As mulheres cadastradas foram: ', end='')
for c in dados:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end= ' ')
print()
print('Lista de pessoas que está acima da média:')
for c in dados:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
        print()
print('\033[1;31mENCERRADO...\033[m')

