# Exercicio 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - a media de idade do grupo
# - qual o nome do homem mais velho
# - quantas mulheres tem menos de 20 anos

print('='*11,'ex056','='*11)
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totmulher20 = 0

for p in range (1,5):
    print('=' * 11,'{}º Pessoa'.format(p),'=' * 11)
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} com menos de 20 anos'.format(totmulher20))