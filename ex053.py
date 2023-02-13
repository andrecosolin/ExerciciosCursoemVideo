# Exercicio 53
# crie um programa que leia uma frase qualquer e diga se ele é um palindromo, desconsiderando os espaços
# EX: apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona

print('='*11,'ex053','='*11)

frase = str(input('Escreva uma frase qualquer: ')).strip().upper().replace(' ', '')
print('O inverso de {}, é : {}'.format(frase, frase[::-1]))
if frase == frase[: :-1]:
    print('Estra frase é um políndromo')
else:
    print('Está frase não é um políndromo')

# feito no video
# frase = str(input('Digite uma frase')).strip.upper()
# palavra = frase.split()
# junto = ''.join(palavra)
# inverso = ''
# for letra in range(len(junto)) - 1, -1, -1):
#     inverso += junto[letra]
# if inverso == junto:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo')