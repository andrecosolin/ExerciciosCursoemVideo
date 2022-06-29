#ex006
#crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e raiz quadrada.

print('='*11,'ex006','='*11)

n = int(input('Digite um número: '))
print('Seu dobro é: {}\nSeu triplo é: {}\nA raiz quadrada é: {:.6}'.format(n*2, n*3, n**(1/2)))

# feito na aula
# n = int((input('Digite um número: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}.'.format(n, d))
# print('O triplo de {} vale {}. \nA rais quadrada de {} é igual a {:.2f}.'.format(n, t, n ,r))
