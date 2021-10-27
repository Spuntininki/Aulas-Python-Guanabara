def voto(nasc):
    from datetime import date
    print(f'com {date.today().year - nasc} anos:')
    if date.today().year - nasc >= 18 and date.today().year - nasc < 70:
        return 'O VOTO É OBRIGATÓRIO'
    elif date.today().year - nasc <= 16 or date.today().year - nasc >= 70:
        return 'O VOTO É OPCIONAL'
    else:
        return 'NÃO PODE VOTAR - MENOR DE IDADE'


data = int(input('Digite sua data de nascimento: '))
opcao = voto(data)
print(opcao)