# ex019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

print('='*11,'ex019','='*11)
import random

p = str(input('Primeiro Aluno: '))
s = str(input('Segundo Aluno: '))
t = str(input('Terceiro Aluno: '))
q = str(input('Quarto Aluno: '))
lista = [p, s, t, q]
escolhido = random.choice(lista)
print("O escolhido foi {}".format(escolhido))