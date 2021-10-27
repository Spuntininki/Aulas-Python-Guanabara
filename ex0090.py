aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] <= 5:
    aluno['situacao'] = '\033[1;31mREPROVADO\033[m'
elif aluno['media'] < 7:
    aluno['situacao'] = '\033[1;33mRECUPERAÇÃO\033[m'
else:
    aluno['situacao'] = '\033[1;32mAPROVADO\033[m'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')