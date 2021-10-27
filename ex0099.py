from time import sleep


def maior(*x):
    m = 0
    for c in range(0, len(x)):
        if c == 0:
            m = x[c]
        else:
            if x[c] > m:
                m = x[c]
        sleep(0.3)
        print(f'{x[c]} ', end='')
    print()
    print(f'O maior número foi {m}')
    print(f'Foi passado {len(x)} valores ao todo')


maior(98, 54, 3, 45, 10)
print('-'*30)
maior(10, 7, 6, 54, 3, 2, 134)
print('-'*30)
maior()
print('-'*30)
maior(9, 9, 2, 3, 4, 1)
print('-'*30)
maior(6)
print('-'*30)