# ex013
# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu salário R$: '))
a = s*0.15
print('Seu salário com aumento de 15% é: {:.2f}'.format(s+a))

# feito no curso
# salário = float(input('Qual é o salário do funcionário? R$ '))
# novo = salário + (salário * 15 / 100)
# print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
