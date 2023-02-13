# Exercicio 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

print('='*11,'ex054','='*11)

# from datetime import date
# ano = date.today().year
# count = 0
# for c in range(1,7+1):
#     num = int(input('Digite o ano de nascimento das pessoas: '))
#     idade = ano - num
# if idade >= 18:
#     print('As pessoas do ano {} já são maior de idade'.format(c))
# else:
#     print('As pessoas do ano {} não atingiram a maioridade'.format(c))

# feito na aula
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
