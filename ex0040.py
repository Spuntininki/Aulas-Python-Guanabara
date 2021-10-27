n1 = float(input('Insira a primeira Nota: '))
n2 = float(input('Insira a segunda Nota: '))
media = (n1+n2)/2
if media <= 5:
    print('\033[1;31mREPROVADO\033[m')
elif media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
