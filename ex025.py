#Exercicio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('='*11, 'ex025', '='*11)

nome = str(input('Qual o seu nome completo: ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))

#feito em aula
# nome = str(input('Qual o seu nome completo: ')).strip()
# print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))