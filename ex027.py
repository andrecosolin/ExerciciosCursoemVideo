# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('='*11, 'ex027', '='*11)
nome = str(input('Escreva o seu nome: ')).strip().title().split()
print('Prazer em conhece-lo(a)')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu útimo nome é: {}'.format(nome[-1]))

# Feito em aula
# nome = str(input('Escreva o seu nome: ')).strip()
# print('Muito prazer te conhecer!)
# print('Seu primeiro nome é: {}'.format(nome[0]))
# print('Seu útimo nome é: {}'.format(nome[len(nome)-1]))