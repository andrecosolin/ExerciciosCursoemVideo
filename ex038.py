# Exercicio 38

# Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('='*11,'ex038','='*11)

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')