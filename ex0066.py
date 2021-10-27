c = s = 0
while True:
    n = int(input('Digite um valor (\033[1;31m999 para parar\033[m): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foi digitado um total de {c} e a soma entre eles resultou em {s}')