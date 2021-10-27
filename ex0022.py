nome = str(input('Qual o seu nome?')).strip()



print('O seu nome em maiuscullo {},\n '
      'em minusculo {},\n'
      'quantidade de caracteres nome inteiro {},\n'
      'quantidade de caracteres primeiro nome {}'.format(nome.upper(), nome.lower(), len(nome)-nome.count(' ', 0), nome.find(' ', 0)))