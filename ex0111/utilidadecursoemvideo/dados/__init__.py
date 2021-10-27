def leiaDinheiro(frase):
    from ex0111.utilidadecursoemvideo import moeda
    while True:
        n = str(input(frase)).strip()
        if n.isnumeric():
            moeda.resumo(float(n))
            break
        elif len(n) <= 2:
            print('\033[1;31mInsira um valor Válido!\033[m')
        elif n[-3] in ',.' and n[-2:].isnumeric() and n[:-3].isnumeric():
            n2 = ''
            for c in n:
                if c != ',':
                    n2 += c
                else:
                    n2 += '.'
            n2 = float(n2)
            moeda.resumo(n2)
            break
        else:
            print('\033[1;31mInsira um valor Válido!\033[m')


def leiaint(frase):
    while True:
        try:
            n = str(input(frase))
            if n != '':
                return int(n)
            else:
                n = 0
                print('\033[1;31mO usuário resolveu não digitar esse número.\033[m')
                return n
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, Digite um número valido.\033[m')




def leiafloat(frase):
    while True:
        try:
            n = str(input(frase))
            if n != '':
                return float(n)
            else:
                n = 0
                print('\033[1;31mO usuário resolveu não digitar esse número.\033[m')
                return n
        except:
            print('\033[1;31mPor favor, Digite um número valido.\033[m')
