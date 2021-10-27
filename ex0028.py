from random import randint
from time import sleep
import colorsys
print('Estou pensando em um nomero de 0 a 5, tente advinhar >:D')
n = randint(0, 5)
print('\033[1;33mPROCESSANDO....\033[m')
sleep(1)
us = int(input('Qual é o numero que eu estou pensando?? '))
if us == n:
    print('\033[1;32mParabens Você acertou!!! o numero que pensei é de fato {}\033[m'.format(n))
else:
    print('\033[1;31mErrou!! HAHAHAHAHHAHA >:D o numero correto era {}\033[m'.format(n))