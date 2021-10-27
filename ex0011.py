#Faça um programa que leia a altura e a largura de uma parede em metros,calcule sua área e
# a quantidade necessaria de tinta para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m**2

alt = float(input('insira a altura da parede em metros: '))
larg = float(input('insira a largura da parede em metros'))
area = alt*larg
print('a area da sua parede resulta em {}'.format(area))
tinta = area/2
print('para pintar essa parede você precisará de {}l de tinta'.format(tinta))

