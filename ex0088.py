from random import randint
from time import sleep
megasena = []
jogos = int(input('Quantos jogos você quer sortear? '))
for c in range(0, jogos):
    megasena.append([])
for c in range(0, jogos):
    for t in range(0, 6):
        n = randint(1, 60)
        while True:
            if n in megasena[c]:
                n = randint(1, 60)
            elif n not in megasena[c]:
                megasena[c].append(n)
                break
    megasena[c].sort()
for pos, c in enumerate(megasena):
    print(f'Jogo {pos+1}: {megasena[pos]}')
    sleep(1)