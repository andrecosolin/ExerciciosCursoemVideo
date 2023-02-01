# Exercicio 39

# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar quanto tempo que falta ou que passou do prazo.

print('='*11,'ex039','='*11)

from datetime import date
nasceu = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasceu
print('De acordo com sua idade {}'.format(idade))
if idade < 18:
    print('Você ainda vai se alistar no serviço militar!')
    print('Falta {} anos para se alistar, que será em {}'.format(18-idade, ano + (18-idade)))
elif idade == 18:
    print('É hora de se alistar no serviço militar!')
elif idade > 18:
    print('Já passou o tempo de alistamento!')
    print('O tempo que passou do prazo foi de {} anos, era pra ter se alistado em {}'.format(idade-18, ano-(idade-18)))

