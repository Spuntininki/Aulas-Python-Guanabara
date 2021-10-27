def escreva(frase):
    print('~'*(len(frase)+4))
    print(f'{frase:^{len(frase)+4}}')
    print('~'*(len(frase)+4))


escreva('Olá mundo!')
