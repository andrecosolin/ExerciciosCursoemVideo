# ex017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


print('='*11,'ex017','='*11)

# import math
# CO = float(input('Digite o valor do cateto oposto: '))
# CA = float(input('Digite o valor do cateto adjacente: '))
# H = (CA**2)+(CO**2)
# print('O comprimento da Hipotenusa é: {:.2f}'.format(math.sqrt(H)))

# FEITO NO CURSO
#maneira matematica
# CO = float(input('Digite o valor do cateto oposto: '))
# CA = float(input('Digite o valor do cateto adjacente: '))
# H = (CA**2)+(CO**2) **(1/2)
# print('O comprimento da Hipotenusa é: {:.2f}'.format(H))

#importanto modulos

# import math
# CO = float(input('Digite o valor do cateto oposto: '))
# CA = float(input('Digite o valor do cateto adjacente: '))
# H = math.hypot(CA, CO)
# print('O comprimento da Hipotenusa é {:.2f}'.format(H))

from math import hypot
CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))
H = hypot(CA, CO)
print('O comprimento da Hipotenusa é {:.2f}'.format(H))

