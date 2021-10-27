from time import sleep
print('PROGRAMA QUE MOSTRA NUMEROS PARES DE 1 A 50')

for c in range(1, 50+1):
    print('.', end=' ')#apenas para mostrar quantas vezes o contador executou
    if c % 2 == 0:
        print(c, end=' ')
    sleep(0.2)
print(' ')
#nesse codigo acima o comando de repetição executa ações desnecessarias..
#no comando abaixo é uma forma que ocupa bem menos memoria de processamento:
for c in range (2, 50+1, 2): #para mim fica mais facil de entender tendo como base que vai inicar no numero 2 e vai
    print(c, end= ' ')#somar de 2 em 2, assim caso eu queira mostrar a tabuada do 3 por exemplo eu colocaria algo como 'in range(3, 61, 3)'