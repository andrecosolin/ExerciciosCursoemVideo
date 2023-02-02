# Exercicio 44

# Elabore o programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro ou pix: 10% de desconto
# - á vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('='*11,'ex044','='*11)

# Vproduto = float(input('Digite o Valor do produto: R$ '))
# print('''Qual a forma de pagamento:
# [1] - Dinheiro ou Pix: 10% de desconto
# [2] - Á vista no Cartão: 5% de desconto
# [3] - 2x no Cartão: preço normal
# [4] - 3x ou mais no Cartão: 20% de juros''')
# condição = int(input('Qual forma de pagamento desejada: '))
# if condição == 1:
#     Avista = Vproduto - (Vproduto * 0.1)
#     print('Obrigado, o valor total do produto é de R${:.2f}'.format(Avista))
# elif condição == 2:
#     cartão = Vproduto - (Vproduto * 0.05)
#     print('Obrigado, o valor total do produto é de R${:.2f}'.format(cartão))
# elif condição == 3:
#     total = Vproduto / 2
#     print('Obrigado, o valor total do produto é de R${:.2f}'.format(Vproduto))
#     print('Sua parcela será de R${:.2f} em 2 vezes'.format(total))
# else:
#     vezes = int(input('Quantas parcelas: '))
#     parcelado = Vproduto + (Vproduto * 0.2)
#     total = parcelado / vezes
#     print('O valor total do produto é de R${:.2f}'.format(parcelado))
#     print('Sua parcela será de R${:.2f} em {} vezes'.format(total, vezes))

# outra forma:
Vproduto = float(input('Digite o Valor do produto: R$ '))
print('''Qual a forma de pagamento:
[1] - Dinheiro ou Pix: 10% de desconto
[2] - Á vista no Cartão: 5% de desconto
[3] - 2x no Cartão: preço normal
[4] - 3x ou mais no Cartão: 20% de juros''')
condição = int(input('Qual forma de pagamento desejada: '))
if condição == 1:
    total = Vproduto - (Vproduto * 0.1)
elif condição == 2:
    total = Vproduto - (Vproduto * 0.05)
elif condição == 3:
    total = Vproduto
    cartão = Vproduto / 2
    print('Sua parcela será de R${:.2f} em 2 vezes'.format(cartão))
elif condição == 4:
    vezes = int(input('Quantas parcelas: '))
    total = Vproduto + (Vproduto * 0.2)
    parcela = total / vezes
    print('Sua parcela será de R${:.2f} em {} vezes'.format(parcela, vezes))
else:
    total = 0
    print('OPÇÃO inválida, escolha entre as opções acima!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(Vproduto, total))