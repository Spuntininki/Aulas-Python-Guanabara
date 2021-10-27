def fatorial(num, show=False):
    """
    ->Faz o calculo fatorial de um número
    :param num: define o número a ser feito o calculo fatorial
    :param show: escolhe se vai ou não aparecer o processo de calculo fatorial
    :return: sem retorno
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c} ', end='X ')
            else:
                print(f'{c} ', end='= ')

    print(f'{f}')


fatorial(5, True)
help(fatorial)