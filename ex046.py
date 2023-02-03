# Exercicio 46

# Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print('='*11,'ex046','='*11)

import time
print('=-'*10,'VAI COMEÇAR A CONTAGEM REGRESSIVA','=-'*10)
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print('fim')

# do video
# from time import sleep
# for cont in range(10, -1, -1):
#     print(cont)
#     sleep(0.5)
# print('BUM! BUM! POOOW')