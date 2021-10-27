def ficha():
    nome = str(input('Digite o nome do jogador: ')).strip()
    gols = str(input('Digite a quantidade de gols: ')).strip()
    if nome == '' and gols.isnumeric():
        nome = '<desconhecido>'
        print(f'O jogador {nome} marcou {gols} gol(ls) no campeonato')
    elif nome != '' and gols.isnumeric():
        print(f'O jogador {nome} marcou {gols} gol(ls) no campeonato')
    else:
        nome = '<desconhecido>'
        gols = '0'
        print(f'O jogador {nome} marcou {gols} gol(ls) no campeonato')

ficha()