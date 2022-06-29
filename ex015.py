# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('='*11,'ex015','='*11)

dias = int(input('Quantos dias alugados: '))
km = int(input('Quantos km rodados: '))
preço = (60 * dias) + (0.15 * km)
print('O preço a pagar é R$ {:.2f}'.format(preço))


