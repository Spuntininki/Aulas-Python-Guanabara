def leiaint(frase):
    while True :
        núm = str(input(frase))
        if núm.isnumeric():
            return núm
        else:
            print('\033[1;31mDigite um número inteiro valido! tente novamente.\033[m')


numero = leiaint('Digite um número inteiro qualquer: ')
print(f'Você digitou o número {numero}')
