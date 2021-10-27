from math import sin, cos, tan, radians
an = float(input('Insira o angulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('o algulo digitado foi {}°'.format(an))
print('seu seno corresponde a: {:.2f}'.format(sen))
print('seu cosseno corresponde a: {:.2f}'.format(cos))
print('sua tangente corresponde a: {:.2f}'.format(tan))
