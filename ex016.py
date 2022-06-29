# ex016
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: digite um numero 6.127, esse número tem a parte inteira 6.

print('='*11,'ex016','='*11)

import math
numero = float(input('Digite qualquer número: '))
print('Sua porção inteira é: {}'.format(math.trunc(numero)))

