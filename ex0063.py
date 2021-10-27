#sequencia fibonacci
n1 = int(input('Insira quantos elementos da sequencia fibonacci você quer ver: '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
print('{} -> '.format(t1), end='')
print('{} -> '.format(t2), end='')
while c <= n1:
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    c += 1
print('FIM')