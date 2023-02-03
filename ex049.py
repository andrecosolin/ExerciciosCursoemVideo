# Exercicio 49

# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

print('='*11,'ex049','='*11)

n = int(input('Tabuada do número: '))
for count in range(1, 11):
    tab = (n * count)
    print('{} x {} = {}'.format(n, count, tab))