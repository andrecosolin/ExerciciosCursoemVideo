# Exercicio 45

# Crie um programa que faça o computador jogar jokempô com você.

print('='*11,'ex045','='*11)
from random import randint
from time import sleep
print('=-'*10, 'VAMOS JOGAR JOKEMPÔ', '=-'*10)
print('Estou animado para ver quem vai vencer!')
print('Escolha PEDRA, PAPEL OU TESOURA !!! ')
print('NÃO VALE ROUBAR, EU SEI QUE PASSOU PELA SUA CABEÇA')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções
[0] - pedra
[1] - papel
[2] - tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador >= 3:
    print('Jogada inválida, tente novamente!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('|-'*11,'|-'*11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('|-'*11,'|-'*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
