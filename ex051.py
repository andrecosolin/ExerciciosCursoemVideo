# Exercicio 51

# Desenvolva um programa que leia o primeiro termo e a razão de um PA(progressão aritimética) no final, mostre os 10 primeiros termos dessa progressão.
# formula geral da PA = an = a1 + (n – 1)r

print('='*11,'ex051','='*11)

PrimeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = PrimeiroTermo + (10 - 1) * razao
for count in range(PrimeiroTermo, decimo + razao, razao):
    print('{}'.format(count), end=' → ')
print('Fim')