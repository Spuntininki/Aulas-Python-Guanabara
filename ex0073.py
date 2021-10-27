tabela = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atletico-GO', 'Athletico-PR', 'Ceará SC', 'Cuiabá', 'Internacional', 'Fluminense', 'Santos', 'Juventude', 'São Paulo', 'Bahia', 'America-MG', 'Sport Recife', 'Grêmio', 'Chapecoense')
print(f'Segue os 5 primeiros colocados na tablema do campeonato brasileiro:')
for pos, c in enumerate(tabela[0: 5]):
    print(f'{pos+1}°-{c}')
print('-'*30)
print(f'Segue os 4 ultimos colocados da tabela:')
posinv = 20
for pos, c in enumerate(tabela[:-5:-1]):
    pos = posinv - (pos+1)
    print(f'{pos+1}°-{c}')
print('-'*30)
print(f'Segue a lista em ordem alfabetica:')
for pos, c in enumerate(sorted(tabela)):
    print(f'{pos+1}º-{c}')
print('-'*30)
pos = tabela.index('Chapecoense')+ 1
print(f'A Chapecoense se encontra na {pos}ª posição')