# até 9 anos: Mirim
# até 14 anos: infantil
#até 19 anos: Junior
#até 20 anos: senior
# acima: master
from datetime import date
ano = int(input('Qual o seu ano de nascimento?'))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('é um atleta MIRIM')
elif idade <= 14:
    print('É UM atleta da categoria INFANTIL')
elif idade <= 19:
    print('É um atleta da categoria JUNIOR')
elif idade <= 25:
    print('É um atleta da categoria SENIOR')
elif idade > 25:
    print('É um atleta MASTER FUCKER')
