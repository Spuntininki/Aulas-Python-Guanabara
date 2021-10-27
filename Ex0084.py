pessoas = []
dados = []
maiorpeso = menorpeso =  0
nomemaior = []
nomemenor = []
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        nomemaior.append(dados[0])
        nomemenor.append(dados[0])
        maiorpeso = dados[1]
        menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            nomemaior.clear()
            nomemaior.append(dados[0])
            maiorpeso = dados[1]
        elif dados[1] == maiorpeso:
            nomemaior.append(dados[0])
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            nomemenor.clear()
            nomemenor.append(dados[0])
            menorpeso = dados[1]
        elif dados[1] == menorpeso:
            nomemenor.append(dados[0])
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N]')).strip()[0]
    if opcao in 'Nn':
        break
print(f'Aqualtidade de pessoas cadastras foi de {len(pessoas)}')
print(f'A pessoa com o maior peso é de {maiorpeso}KG que é pertencente á: {nomemaior}')
print(f'A pessoa com o menor peso é de {menorpeso}KG que é pertencente á: {nomemenor}')