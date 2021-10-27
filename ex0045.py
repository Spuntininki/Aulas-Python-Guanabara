from random import shuffle, randint
from time import sleep
print('\033[1;33m-=-'*20)
print('JOKENPO!!!!')
print('-=-'*20, '\033[m')
#SOLUÇÃO GUANABARA:
opcao = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[0] PARA PEDRA 
[1] PARA PAPEL  
[2] PARA TESOURA''')
j = int(input('DIGITE SUA ESCOLHA:'))
if j > 2:
    print('\033[1;31mOPÇÃO INVALIDA!\033[m')
else:
    print('\033[1;32m-=-' * 20)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    print('-=-' * 20, '\033[m')
    sleep(0.7)
    print('O computador escolheu {} \nO jogador escolheu {}'.format(opcao[computador], opcao[j]))
if computador == 0:
    if j == 0:
        print('\033[1;33mEMPATE\033[m')
    elif j == 1:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif j == 2:
        print('\033[1;31mMAQUINA VENCEU\033[m')


if computador == 1:
    if j == 0:
        print('\033[1;32mMAQUINA VENCEU\033[m')
    elif j == 1:
        print('\033[1;33mEMPATE\033[m')
    elif j == 2:
        print('\033[1;31mJOGADOR VENCEU\033[m')

if computador == 2:
    if j == 0:
        print('\033[1;31mMAQUINA VENCEU\033[m')
    elif j == 1:
        print('\033[1;32JOGADOR VENCEU\033[m')
    elif j == 2:
        print('\033[1;33mEMPATE\033[m')












#MINHA SOLUÇÃO:
'''m = ['PEDRA', 'PAPEL', 'TESOURA']
shuffle(m)
print('SUAS OPÇÕES:
[1] PARA PEDRA 
[2] PARA PAPEL  
[3] PARA TESOURA')
j = int(input('DIGITE SUA ESCOLHA:'))
if j == 1:
    j = 'PEDRA'
elif j== 2:
    j = 'PAPEL'
elif j == 3:
    j = 'TESOURA'
else:
    print('\033[1;31mInsira uma opção valida!\033[m')




print('VOCÊ ESCOLHEU {} E O COMPUTADOR ESCOLHEU {}'.format(j, m[1]))
if j == 'PEDRA' and m[1] == 'TESOURA':
    print('O JOGADOR VENCEU')
elif j == 'PAPEL' and m[1] == 'PEDRA':
    print('O JOGADOR VENCEU')
elif j == 'TESOURA' and  m[1] == 'PAPEL':
    print('O JOGADOR VENCEU')

if m[1] == 'PEDRA' and j == 'TESOURA':
    print('A MAQUINA VENCEU')
elif m[1] == 'PAPEL' and j == 'PEDRA':
    print('A MAQUINA VENCEU')
elif m[1] == 'TESOURA' and j == 'PAPEL':
    print('A MAQUINA VENCEU')

if j == 'PEDRA' and m[1] == 'PEDRA':
    print('EMPATE')
elif j == 'PAPEL' and m[1] == 'PAPEL':
    print('EMPATE')
elif j == 'TESOURA' and m[1] == 'TESOURA':
    print('EMPATE')'''




