# Exercicio 33

# Faça um programa que leia trés números e mostre qual é o maior e qual é o menor.

print('='*11, 'ex033','='*11)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('o maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
