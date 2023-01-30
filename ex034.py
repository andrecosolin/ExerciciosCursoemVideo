# Exercicio 34

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

print('='*11, 'ex034','='*11)

salario = float(input('Qual o seu salário: '))
if salario >=1250:
    print('Você terá um aumento de 10%, subindo para R${:.2f}'.format(salario + (salario*0.1)))
else:
    print('O aumento do seu salário é de 15%, subindo para R${:.2f}'.format(salario +(salario*0.15)))

#if salario <=1250:
    #novo = salario + (salario * 15 / 100)
#else:
    #novo = salario + (salario * 10 / 100)
#print( 'Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'format.(salario, novo))