from time import sleep
lista = []
c = 0
while True:
    nome = str(input('Digite o Nome do Aluno: ')).capitalize()
    lista.append([])
    lista[c].append(nome)
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    lista[c].append([])
    lista[c][1].append(nota1)
    lista[c][1].append(nota2)
    opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    c += 1
    if opcao in 'N':
        break
print('-'*40)
print('\033[1;32m{:<4} {:<10} {:>8}\033[m'.format('N°', 'NOME', 'MÉDIA'))
print('-'*40)
for pos, c in enumerate(lista):
    print(f'{pos:<4}{c[0]:<10}{(c[1][0] + c[1][1]) /2:>10.1f} ')
while True:
    opcao = int(input('Mostrar a nota de qual aluno? (999 interromper)'))
    if opcao == 999:
        break
    elif opcao < len(lista):
        print(f'Notas de {lista[opcao][0]} é: {lista[opcao][1]}')
    else:
        print('\033[1;31mAluno não encontrado! TENTE NOVAMENTE.\033[m')
print('FINALIZANDO...')
sleep(1)
print('<'*5, 'OBRIGADO VOLTE SEMPRE!', '>'*5)

