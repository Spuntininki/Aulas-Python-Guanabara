from datetime import date
dados = {}
dados['Nome'] = str(input('Insira o nome: '))
anonasc = int(input('Insira o ano de nascimento: '))
dados['Idade'] = date.today().year - anonasc
dados['ctps'] = int(input('Digite o número da carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário: '))
    dados['Aposentadoria'] =dados['Idade'] + (35 - (date.today().year - dados['Ano de contratação']))
for k, v in dados.items():
    print(f'{k} tem o valor {v}')