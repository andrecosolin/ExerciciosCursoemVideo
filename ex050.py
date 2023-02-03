# Exercicio 50

# Desenvolva um programa que leia seis numero inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidere-o

print('='*11,'ex050','='*11)

# soma = 0
# for count in range(1,7):
#     n = int(input('Digite um números: '))
#     if n % 2 ==0:
#         soma += n
# print('A soma dos número pares que digitou é de: {}'.format(soma))

# feito na aula
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))


