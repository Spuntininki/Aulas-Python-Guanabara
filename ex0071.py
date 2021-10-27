#simulador de caixa eletronico
# NOTA: considerar que o caixa possui notas apenas de 50 20 10 e 1.
print('-'*30)
print('BANCO DEV')
print('-'*30)
saque = float(input('Digite o valor do saque: R$'))
total = saque
cedula = 50
contcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        contcedula += 1
    else:
        if contcedula > 0:
            print(f'{contcedula} de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contcedula = 0
        if total == 0:
            break



#solução matematica:
'''ced50 = ced20 = ced10 = ced1 = 0
saque = int(input('Digite o valor que quer sacar: '))
ced50 = saque // 50
saque = saque - (ced50 * 50)
ced20 = saque // 20
saque = saque - (ced20 * 20)
ced10 = saque // 10
saque = saque - (ced10 * 10)
ced1 = saque // 1
saque = saque - (ced1 * 1)
if ced50 > 0:
    print(f'Total de {ced50} cedulas de 50')
if ced20 > 0:
    print(f'{ced20} cedulas de 20')
if ced10 > 0:
    print(f'{ced10} cedulas de 10')
if ced1 > 0:
    print(f'{ced1} cedulas de 1')
'''
