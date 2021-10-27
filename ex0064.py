c = n = i = 0
soma = int(0)
while c == 0:
    n = int(input('Insira um número: '))
    if n != 999:
        i += 1
        soma = soma + n
    if n == 999:
        c = 1
print('Você digitou {} números e a soma entre eles é {}'.format(i, soma))
