# Exercicio 42

# Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('='*11,'ex042','='*11)

# from time import sleep
# print('=-'*11,'ANALISADOR DE TRIÂNGULO','=-'*11)
# lado1 = float(input('Digita primeiro valor: '))
# lado2 = float(input('Digita segundo valor: '))
# lado3 = float(input('Digita terceiro valor: '))
# print('ANALIZANDO...')
# sleep(3)
# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1 and lado1 == lado2 == lado3:
#     print('O valor das retas formam um triângulo!')
#     print('O triângulo será um EQUILÁTERO')
#     print('todos os lados iguais')
# elif lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1 and lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
#     print('O valor das retas formam um triângulo!')
#     print('O triângulo será um ISÓCELES')
#     print('dois lados iguais')
# elif lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1 and lado1 != lado2 != lado3:
#     print('O valor das retas formam um triângulo!')
#     print('O triângulo será um ESCALENO')
#     print('todos os lados diferentes')
# else:
#     print('O valor das retas não formam um triângulo!')

# outra forma:
lado1 = float(input('Digita primeiro valor: '))
lado2 = float(input('Digita primeiro valor: '))
lado3 = float(input('Digita primeiro valor: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    print('O valor das retas formam um triângulo!')
    if lado1 == lado2 == lado3:
        print('O triângulo será um EQUILÁTERO')
        print('todos os lados iguais')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('O triângulo será um ISÓCELES')
        print('dois lados iguais')
    elif lado1 != lado2 != lado3:
        print('O triângulo será um ESCALENO')
        print('todos os lados diferentes')
else:
    print('O valor das retas não formam um triângulo!')