#A frase é um PALINDROMO?

frase = str(input('Escreva uma frase: ')).strip().lower()
print('Você digitou a frase  "{}"'.format(frase.upper()))
frase = frase.replace(' ', '')
i = int(len(frase))
t = i -1
avesso = ''
for c in range(0, i):
      avesso = avesso + frase[t]
      t = t - 1
print('A frase invertida fica "{}"'.format(avesso.upper()))
if avesso == frase:
    print('\033[1;32mA FRASE DIGITADA É UM PALINDROMO!!!!!\033[m')
else:
    print('\033[1;31mA FRASE DIGITADA NÃO É UM PALINDROMO!!!\033[m')



