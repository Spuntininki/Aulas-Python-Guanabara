palavras = ('ovo', 'rato', 'peneu', 'piolho', 'futuro', 'passado')
for c in palavras[0:]:
    print(f'Na palavra {c.upper()} temos: ', end= '')
    for letra in c[0:]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')