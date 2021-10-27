while True:
    n = int(input('Digite o número que gostaria de ver a tabuada (\033[1;31mdigite um número negativo para parar\033[m): '))
    c = 1
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)
print('\033[1;32mObrigado pela preferencia!\033[m')