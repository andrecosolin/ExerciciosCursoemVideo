#ex010
#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$ 1,00 = R$ 3,27

print('='*11,'ex010','='*11)

c = float(input('Digite o valor da sua carteira: '))
print('Você pode comprar US${:.3}'.format(c/3.27))

# feito em aula
# real = float(input('Quanto dinheiro você tem na carteira: '))
# dolar = real / 3.27
# print('Com R${:.2f} você pode comprar US${:.2f}.format(real, dolar))
