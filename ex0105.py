def notas(*notas, sit=False):
    """
    -> Função que recebe varias notas e joga em um dicionario o maior valor, menor valor, quantas notas foram e a media.
    :param notas: recebe varias notas de alunos
    :param sit: caso Verdadeiro irá mostrar a situação do aluno
    :return: irá retornar os dados em dicionario
    """
    alunos = {}
    alunos['Total de Notas'] = len(notas)
    alunos['Maior nota'] = max(notas)
    alunos['Menor nota'] = min(notas)
    alunos['Média'] = sum(notas)/len(notas)
    if sit:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'BOA'
        elif alunos['Média'] >= 5:
            alunos['Situação'] = 'RECUPERAÇÃO'
        else:
            alunos['Situação'] = 'REPROVADO'
    return alunos


resp = notas(5.5, 2.5 , 8.5, sit= True)
print(resp)
help(notas)