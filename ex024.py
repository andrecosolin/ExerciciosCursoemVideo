# Exercicio 24
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print('='*11, 'ex024', '='*11)

cidade = str(input('Digite da cidade que nasceu: ')).strip().upper()
print('Existe a Palavra Santo na cidade que nasceu:','SANTO' in cidade)

# Feito em aula
# cid = str(input('Digite da cidade que nasceu: ')).strip()
# print(cid[:5] == 'Santo')

# cid = str(input('Digite da cidade que nasceu: ')).strip()
# print(cid[:5].upper == 'SANTO')