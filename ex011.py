#ex011
#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('='*11,'ex011','='*11)

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
tinta = area / 2
print('A área da sua parede é de: {}m²'.format(area))
print('A quantidade de tinta para pintar é: {}L'.format(tinta))

# feito no curso
#faltou fazer a variavel de tinta e dividi-la por 2.