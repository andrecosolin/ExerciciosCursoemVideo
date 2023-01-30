# Exercicio 31

# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# E R$0.45 para viagens até mais longas

print('='*11, 'ex031','='*11)

dist = float(input('Qual a distância percorrida em km da viagem: '))
if dist <= 200:
    print('Sua passagem custará R${:.2f}'.format(0.50*dist))
else:
    print('Sua passagem custará R${:.2f}'. format(0.45*dist))