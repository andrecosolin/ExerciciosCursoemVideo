# Exercicio 37

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print('='*11,'ex037','='*11)

num = int(input('Digite um número qualquer: '))
print('''Escolha umas das opções abaixo de conversção para o número digitado, opções:
[1] - para binário
[2] - para octal
[3] - para hexadecimal''')
escolha = int(input('Qual opção escolhida? '))
if escolha == 1:
    binario = "{0:b}".format(num)
    print('O número {} em binário é {}'.format(num, binario))
elif escolha == 2:
    octal = "{0:o}".format(num)
    print('O número {} em octal é {}'.format(num, octal))
elif escolha == 3:
    hex = "{0:x}".format(num)
    print('O número {} em hexadecimal é {}'.format(num, hex))
else:
    print('Você digitou a opção errada, por favor, escolha alguma opção mostrada!')

#Feito na aula video
# num = int(input('Digite um número inteiro: '))
# print('''Escolha uma das bases para conversão
# [1] converter para BINÁRIO
# [2] converter para OCTAL
# [3] converter para HEXADECIMAL''')
# opção = int(input('Sua opção: '))
# if opção == 1:
#     print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
# elif opção == 2:
#     print('{} convertido para OCTAL é igual a {}'.format(num, bin(num)[2:]))
# elif opção == 3:
#     print('{} convertido para HEXADECIMAL é igual a {}'.format(num, bin(num)[2:]))
# else:
#     print('Opção inválida. Tente novamente!')