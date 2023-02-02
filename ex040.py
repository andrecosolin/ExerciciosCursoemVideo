# Exercicio 40

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('='*11,'ex040','='*11)

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
média = (nota1 + nota2) / 2
print('\033[30;44mSua média foi de {:.1} e você está:\033[m'.format(média))
if média < 5.0:
    print('\033[0;30;41mREPROVADO\033[m')
elif média >= 5.0 and média <= 6.9:
    print('\033[1;30;41mDE RECUPERAÇÃO\033[m')
else:
    print('\033[30;42mAPROVADO\033[m')