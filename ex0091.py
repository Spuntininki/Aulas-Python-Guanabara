from random import randint
from time import sleep
from operator import itemgetter
print('\033[1;32mROLAGEM DE DADOS...\033[m')
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)
rank = []
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(rank):
    print(f'{i+1}° colocado foi {c[0]} que tirou {c[1]}')
    sleep(1)