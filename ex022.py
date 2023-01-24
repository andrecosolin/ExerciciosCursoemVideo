# Exercicio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

print('='*11, 'ex022', '='*11)

# nome = input('Digite seu nome: ')
# print(nome)
# nome1 = nome.replace(' ','')
# print(len(nome1))
# print(nome[:5])

# Feito na aula
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é em maiusucula é {}'.format(nome.upper()))
print('Seu nome é em minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
