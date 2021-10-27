#Escreva um programa que leia a data de nascimento de um Jovem e mostre de acordo com sua idade se:
#ele ainda vai se alistar
# se é a hora de se alistar
#se já passou da hora de se alistar
# mostre também quanto tempo falta para se alistar e quanto tempo já passou
from datetime import date
atual = date.today().year
print(atual)
print('\033[1;32m-=-' * 20)
print('ALISTAMENTO MILITAR')
print('-=-' * 20, '\033[m')
sex = int(input('selecione 1 caso mulher 2 caso para homem'))
nasc = int(input('Qual é o ano do nascimento?'))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos de idade em {}'.format(nasc, idade, atual))

if sex == 1:
    print('Você não precisa se alistar, pois é mulher')
elif sex == 2:
    if idade == 18:
        print('Voce precisa se alistar IMEDIATAMENTE')
    elif idade < 18:
        print('Você ainda não chegou na idade de se alistar pois ainda falta {} '
              'anos que será no ano de {}'.format(-(idade - 18), atual + -(idade-18)))
    elif idade > 18:
        print('Já passou o tempo de se alistar  pois hoje você tem {} anos '
              'e você fez 18 anos em {}'.format(idade, atual - (idade - 18)))
else:
    print('Opção invalida!!')

# ao invés de fazer o calculo no format e usado regra de sinal para resolver poderia simplesmente ter feito uma variavel
# ou seja por exemplo: saldo = 18 - idade para o caso o usuario seja um menor ou idade - 18 para o caso do usario ser maior

'''idade = int(input('Qual é a sua Idade?'))
if idade < 18:
    print('ainda não chegou a hora de se alistar pois ainda falta {} anos'.format(-(idade-18)))
elif idade == 18:
    print('Você já está a idade para se alistar, pois já possui {}'.format(idade))
else:
    print('Você já passou da idade de se alistar e isso faz {} anos'.format(-(18-idade)))'''