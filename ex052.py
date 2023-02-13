# Exercicio 52

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
# Um número primo é aquele que é dividido apenas por um e por ele mesmo. Entre 0 e 100 existem apenas 25 números primos.

print('='*11,'ex052','='*11)

n = int(input('Digite um número: '))
total = 0
for count in range(1, n+1):
    if n % count ==0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(count), end=' ')
print('\n\033[mO número {} foi divisel {} vezes'.format(n, total))
if total ==2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')


