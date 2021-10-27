#Escreva um programa  que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#a media de idade do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
mediaidade = 0
hv = ''
idadehv = 0
mv = 0
for c in range(1, 4):
    nome = str(input('Qual o nome da {}° pessoa? '.format(c)))
    idade = int(input('Qual é a idade da {}° pessoa? '.format(c)))
    sexo = str(input('Insira M para homem F para mulher:')).strip().upper()
    mediaidade += idade
    if sexo == 'F' and idade < 20:
        mv += 1
    if c == 1 and sexo == 'M':
        hv = nome
        idadehv += idade
    else:
        if idade > idadehv and sexo == 'M':
            hv = nome
            idadehv = idade
print('A media da Idade do grupo é {}'.format(mediaidade/c))
if hv != '':
    print('O homem mais velho se chama {:.2f}'.format(hv.capitalize()))
else:
    print('Neste grupo não possui homens.')
if mv != 0:
    print('Neste grupo possui um total de {} mulheres abaixo de 20 anos'.format(mv))
else:
    print('Neste grupo todas as mulheres são maiores de 20 anos')
