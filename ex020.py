# ex020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('='*11,'ex020','='*11)

import random

p = str(input('Primeiro nome: '))
s = str(input('Segundo nome: '))
t = str(input('Terceiro nome: '))
q = str(input('Quarto nome: '))

lista = [p, s, t, q]
random.shuffle(lista)
print('A ordem de apresentação do trabalho será {}'.format(lista))