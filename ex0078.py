lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi o {maior} que se encontra nas posições:', end='')
for c, n in enumerate(lista):
  if maior in lista[c:c+1]:
                print(f'{c}..', end='')
print('')
print(f'O menor valor digitado foi o {menor}, que se encontra nas posições:', end='')
for c, n in enumerate(lista):
    if menor in lista[c:c+1]:
        print(f'{c}..', end='')

