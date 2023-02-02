# Exercicio 41

# A confederação nacional de netação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

print('='*11,'ex041','='*11)

from datetime import date
ano = int(input('Qual o seu ano de nasciumento: '))
idade = date.today().year - ano
print('Sua idade é: {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')

# outra forma é:
# from datetime import date
# atual = date.today().year
# idade = atual - nascimento