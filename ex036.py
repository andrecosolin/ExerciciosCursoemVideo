# Exercicios 36

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('='*11,'ex036','='*11)

print('\033[0;34;40mVamos analisar o seus dados para aprovar ou não o empréstimo bancário da compra casa!!!\033[m')
ValorCasa = float(input('Qual o valor da casa? R$ '))
Salario = float(input('Qual o seu salario bruto? R$ '))
Anos = float(input('Em quantos anos deseja pagar o empréstimo? '))
meses = Anos * 12
ValorParcela = ValorCasa / meses
valorsalario = Salario * 0.3
print('O valor da prestação mensal é de R${:.2f} em {:.0f} meses'.format(ValorParcela, meses))
if ValorParcela <= valorsalario:
    print('\033[30;42mPARABÉNS, o seu empréstimo foi aprovado!!\033[m')
elif ValorParcela > valorsalario:
    print('\033[0;30;41mNEGADO, infelizmento não vamos liberar o empréstimo!\033[m')
    print('Tente aumentar o valor do seu salário.')

#feito na aula video
# casa = float(input('Valor da casa: R$'))
# salário = float(input('Salário do comprador: R$'))
# anos = int(input('Quantos anos de financiamento? '))
# prestação = casa / (anos * 12)
# print('Para pagar uma casa de R${:.2f} em {} anos'. format(casa, anos))
# print('A prestação será de R${:.2f}'.format(prestação))
# if prestação <= mínimo:
#     print('O empréstimo pode ser CONCEDIDO!')
# else:
#     print('O empréstimo foi NEGADO!')


