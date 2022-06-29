#ex012
#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('='*11,'ex012','='*11)

p = float(input('Digite o valor do produto R$: '))
d = p * 5 / 100
v = p - d
print('O valor com 5% de desconto é: {:.2f}'.format(v))

# feito no curso
# faltou calcular corretamente a porcentagem.
# era 5 / por 100