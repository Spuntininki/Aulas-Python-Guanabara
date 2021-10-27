print('\033[1;33m-=-' * 20)
print('CALCULO IMC')
print('-=-' * 20, '\033[m')
peso = float(input('Insira o seu PESO: '))
altura = float(input('insira a sua altura: '))
imc = peso/altura**2

print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO')
elif imc >= 18.5 and peso < 25.0:
    print('VOCÈ ESTÁ NO PESO IDEAL')
elif imc >= 25.0 and imc < 30.0:
    print('VOCÊ ESTÁ ACIMA DO PESO')
elif imc >= 30.0 and imc < 40.0:
    print('VOCÊ ESTÁ NA FAIXA DA OBESIDADE')
elif imc >= 40.0:
    print('OBESIDADE MORBIDA')
