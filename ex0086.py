lista = [[], [], []]
for c in range(0, 3):
    for pos in range(0, 3):
        n = int(input(f'Digite o número para [{c}, {pos}]:  '))
        lista[c].append(n)
print('-='* 30)
for t in range(0, 3):
    for pos in range(0, 3):
        print(f'[ {lista[t][pos]:^5} ] ', end='')
    print('')

'''print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')'''
