#crie um programa que mostre o seu dobro, seu triplo  e sua raiz quadrada

n = int(input('insira um valor: '))

print('o dobro do numero {} é {} \nseu triplo é {} \ne sua raiz quadrada é {:.5f}'.format(n, (n*2), (n*3), (n**(1/2))))
#outra maneira de fazer a raiz quadradad no python é chamar a função "pow", exemplo: pow(n, (1/2))
# assim pode se perceber que a base está no N e o expoente vem em seguida
