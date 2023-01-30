# Exercicio 28

# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('='*11, 'ex028','='*11)

import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('='*11,'GAME DA ADIVINHAÇÃO','='*11)
nescolhido = int(input('Digite o número de 0 a 5 que eu pensei: ' ))
print('PROCESSANDO...')
sleep(3)
lista = [0,1,2,3,4,5]
numero = random.choice(lista)
print('O número que eu escolheu foi {}.'.format(numero))
if nescolhido == numero:
    print('Parabéns, você venceu!')
else:
    print('Que pena, você perdeu!')
