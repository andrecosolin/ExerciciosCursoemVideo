# Exercicio 30

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

print('='*11, 'ex030','='*11)

num = int(input('Digite um número: '))
if num % 2 ==0:
    print('O número {} que você digitou é Par'.format(num))
else:
    print('O número {} que você digitou é ímpar'.format(num))