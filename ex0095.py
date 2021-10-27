from time import sleep
jogadores = []
jogador = {}
j = 0
g = []
totgol = 0
while True:
    jogador['nome'] = str(input('Dgigite o nome do jogador: '))
    j = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for c in range(0, j):
        g.append(int(input(f'Quantos gols foram marcados na partida {c}?')))
        totgol += g[c]
    jogador['Gols'] = g[:]
    jogador['TotaldeGols'] = totgol
    j =  totgol = 0
    jogadores.append(jogador.copy())
    g.clear()
    while True:
        opcao = str(input('Deseja continuar? [s/n]')).lower().strip()[0]
        if opcao in 'n':
            break
        else:
            print('-' * 30)
            break
    if opcao in 'n':
        break
print(f'{"cod":<5}{"Nome":<15}{"gols":<15}{"total":>15}')
print(f'-'*60)
for i, c in enumerate(jogadores):
    print(f'{i:<5}{c["nome"]:<15}{str(c["Gols"]):<15}{str(c["TotaldeGols"]):>15}')
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if opcao < len(jogadores):
        print(f'--LEVANTAMENTO do jogador {jogadores[opcao]["nome"]}:')
        for i, c in enumerate(jogadores[opcao]["Gols"]):
            print(f'no jogo {i+1} foi marcado {c} gols')
            sleep(0.5)
    elif opcao == 999:
        print('\033[1;32mFINALIZANDO...')
        sleep(1)
        print('Volte sempre!')
        break
    else:
        print('\033[1;31mJOGADOR NÃO ENCONTRADO. TENTE NOVAMENTE FDP\033[m')

