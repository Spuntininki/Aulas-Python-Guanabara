#faça um programa que leia uma frase e mostre: quantas letras 'a' ela possui; em que posição ela aparece pela primeira vez; e qual posição aparece pela ultima vez;

frase = str(input('Escreva uma frase: ')).strip()
frase = frase.lower()
print('A letra "a" aparece {} vezes, aparece na primeira vez na posição {} '
      'e aparece na ultima vez na posição {}'.format(frase.count('a'), frase.find('a'), frase.rfind('a')))