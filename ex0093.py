jogadores = dict()
jogadores['Nome'] = str(input('Digite o nome do jogador: '))
jogadores['Gols'] = []
jogadores['partidas'] = int(input(f'Digite quantas partidas {jogadores["Nome"]} jogou: '))
totgols = 0
for c in range(0, jogadores['partidas']):
    jogadores['Gols'].append(int(input(f'Quantos gols fez na partida {c}: ')))
    totgols += jogadores['Gols'][c]
jogadores['Total de gols'] = totgols
print('-'*30)
for k, v in jogadores. items():
    print(f'{k} possui o valor de {v}')
print('-'*30)
print(f'O jogador {jogadores["Nome"]} jogou {jogadores["partidas"]} partidas')
for i, c in enumerate(jogadores['Gols']):
    print(f'    => No jogo {i}, fez {c} Gols')
print(f'Fez um total de {totgols} gols')