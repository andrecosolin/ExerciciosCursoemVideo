# Exercicio 29

# Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h.
# Mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.

print('='*11, 'ex029','='*11)

vel = int(input('Digite a velocidade que seu carro passou no radar: '))
multa = (vel - 80) * 7.00
if vel >= 80:
    print('Você estava acima da velocidade permitida, MULTADO!')
    print('O valor da sua multa será de R$7.00 por km acima do limite permitido, assim sua multa é de R${:.2f}'.format(multa))
else:
    print('Felizmente você não foi multado!')
