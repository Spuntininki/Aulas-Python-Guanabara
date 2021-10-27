s = str(input('Digite "M" para masculino e "F" para feminino: ')).upper().strip()[0]

'''while s != 'M' and s != 'F':
    print('\033[1;31m"{}" não é uma opção valida.\033[m'.format(s))
    s = str(input('Tente novamente: ')).upper()
print('\033[1;32mOpção correta\033[m')'''
#solução guanabara
while s not in 'MF':
    s = str(input('Opção invalida por favor tente novamnete: ')).upper().strip()[0]
print('Sexo Registrado {}'.format(s))