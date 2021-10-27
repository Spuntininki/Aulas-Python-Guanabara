#Jogo de advinhar numero 2.0
from random import randint
print('\033[1;33m-=-'*20)
print('TENTE ADVINHAR QUAL NUMERO ESTOU PENSANDO >:D')
print('-=-'*20, '\033[m')
m = randint(0, 10)
n = int(input('Então de 0 a 10 qual numero estou pensando? '))
c = 1
while n != m:
    print('\033[1;31mErrou!\033[m')
    if m < n:
       n = int(input('Um pouco menos, tente novamente: '))
    elif m > n:
        n = int(input('Um pouco mais, tente novamente: '))
    c += 1
if c == 1:
    print('\033[1;32mParabéns! Você acertou na primeira tentativa. \nrealmente o numero que pensei foi {} \033[m'. format(m))
else:
    print('\033[1;32mVocê acertou! realmente o numero que pensei foi {}, \nfoi necessario {} tentativas para acertar \033[m'.format(m, c))