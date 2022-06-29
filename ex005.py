#ex005
#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

print('='*11,'ex005','='*11)
n = int(input('Digite um número: '))
print('Seu sucessor é: {}'.format(n+1))
print('Seu antecessor é: {}'.format(n-1))

# forma que o curso fez
# n = int(input('Digite um número: '))
# print ('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
