# Exercicio 35

# Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo.

from time import sleep
print('='*11, 'ex035','='*11)
print('=-'*11,'ANALISADOR DE TRIÂNGULO','=-'*11)

lado1 = float(input('Digita primeiro valor: '))
lado2 = float(input('Digita segundo valor: '))
lado3 = float(input('Digita terceiro valor: '))
print('ANALIZANDO...')
sleep(3)
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    print('O valor das retas formam um triângulo!')
else:
    print('O valor das retas não formam um triângulo!')
