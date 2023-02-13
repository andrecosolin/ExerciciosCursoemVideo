# Exercicio 55
# Faça um programa que lê o peso de cinco pessoas e no final mostre qual foi o maior e menor peso lido

print('='*11,'ex055','='*11)
pmaior = 0
pmenor = 0
for p in range (1,6):
    peso = float(input('Digite o peso (KG) da {}° pessoa: '.format(p)))
    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso lido é de {} KG.'.format(pmaior))
print('O menor peso lido é de {} KG.'.format(pmenor))

