def aumentar(valor, percent, format = False):
    """

    :param valor: recebe o valor desejado
    :return: retorna o valor com 10% de aumento
    :percent: Define o percentual de aumento
     :format: se TRUE retorna o valor formatado como moeda (2 casas após a virgula)
    """
    if format:
        return f'{fmoeda(valor + (valor * percent / 100))}'
    else:
        return valor + (valor * percent /100)


def diminuir(valor, percent, format = False):
    """

    :param valor: recebe o valor desejado
    :return: retorna o valor com 10% de desconto
    :percent: Define o percentual de aumento
    :format: se TRUE retorna o valor formatado como moeda (2 casas após a virgula)
    """
    if format:
        return f'{fmoeda(valor - (valor*percent/100))}'
    else:
        return valor - (valor * percent/100)


def dobro(valor, format = False):
    """

    :param valor: recebe o valor desejado
    :return: retorna o valor dobrado
     :format: se TRUE retorna o valor formatado como moeda (2 casas após a virgula)
    """
    if format:
        return f'{fmoeda(valor * 2)}'
    else:
        return valor * 2


def metade(valor, format=False):
    """

    :param valor: recebe o valor desejado
    :return: retorna o valor pela metade
     :format: se TRUE retorna o valor formatado como moeda (2 casas após a virgula)
    """
    if format:
        return f'{fmoeda(valor/2)}'
    else:
        return valor / 2


def fmoeda(valor, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(num, aum = 0, dim = 0):
    print('-'*30)
    print(f'{"ANALISANDO DADOS":^30}')
    print('-'*30)
    print(f'Preço analisado:\t{fmoeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, format=True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    if aum != 0:
        print(f'{aum}% de aumento: \t{aumentar(num, aum, True)}')
    if dim != 0:
        print(f'{dim}% de desconto: \t{diminuir(num, dim, True)}')
    print('-'*30)