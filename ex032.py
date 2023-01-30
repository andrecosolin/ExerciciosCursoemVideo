# Exercicio 32

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
# Para determinar se um ano é bissexto, execute estas etapas:
# Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# O ano é bissexto (tem 366 dias).
# O ano não é um ano bissexto (tem 365 dias).

print('='*11, 'ex032','='*11)
from datetime import date
ano = int(input('Digite um ano qualquer para saber se ele é bissexto, ou 0 para o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
            print('Que legal, o ano digitado {}, é bissexto!'.format(ano))
else:
    print('O ano digitado {} não é bissexto!!'.format(ano))


