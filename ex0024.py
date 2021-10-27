#Escreva um programa que leia o nome de uma cidade mostre se ela começa com a palavra 'SANTO'

nome = str(input('Insira o Nome da Cidade: ')).strip()
#nome = nome.upper()
#print('SANTO' in nome[0:5])
#RESOLUÇÃO GUANABARA:
print(nome[:5].upper() == 'SANTO')