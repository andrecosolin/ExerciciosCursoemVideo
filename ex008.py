#ex008
#escreva um programa que leia um valor em metros e o exiba ele convertido em centimetros e milimetros

print('='*11,'Ex008','='*11)

n = float(input('Digite um número: '))
print('centímetro: {:.0f} cm'.format(n*100))
print('milímetro: {:.0f} mm'.format(n*1000))

# feito no curso
# medida = float(input('Uma distância em metros: ')
# cm = medida * 100
# mm = medida * 1000
# print('A medida de {}m corresponde a {}cn e {}mm'.format(medida, cm, mm))
