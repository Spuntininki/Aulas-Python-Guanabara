expressão = str(input('Digite um expressão: '))
parentesesabri = 0
parentesesfecha = 0
for c in expressão:
    if c == '(':
        parentesesabri += 1
    if c == ')':
        parentesesfecha += 1
parenteses = parentesesfecha + parentesesfecha
if parenteses % 2 == 0 and parentesesfecha == parentesesabri:
    print('\033[1;32mEssa é uma expressão valida!\033[m')
else:
    print('\033[1;31mEssa é uma expressão invalida!\033[m')
