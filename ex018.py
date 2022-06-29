# ex017
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('='*11,'ex018','='*11)

# import math
# angulo = float(input('Digite o ângulo que você deseja: '))
# seno = math.sin(math.radians(angulo))
# cosseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))
# print('O angulo de {:.0f} tem o SENO de {:.2f}'.format(angulo, seno))
# print('O angulo de {:.0f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
# print('O angulo de {:.0f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {:.0f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {:.0f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {:.0f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

