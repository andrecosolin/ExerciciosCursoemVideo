#n = float(input('Digite um valor: '))
#print(n)

#n = float(input('Digite um valor: '))
#print(type(n)) #type mostra o que é a váriavel

#n = bool(input('Digite um valor: '))
#print(n)

#n = input('Digite um valor: ')
#print(n.isalnum())

#n = input('Digite um valor: ')
#print(n.isnumeric())

# print('===========EX004===========')
# p = input('Digite algo: ')
# print('O tipo primitivo desse valor é: {0}'.format(type(p)))
# print('Só tem espaços?',p.isspace())
# print('É número?',p.isnumeric())
# print('É alfabético?',p.isalpha())
# print('É alfanúmerico?',p.isalnum())
# print('Está em maiuscula?',p.isupper())
# print('Está em minúscula?',p.islower())
# print('Está capitalizada?',p.isdigit())

# print('===========EX004===========')
# p = input('Digite algo: ')
# print('O tipo primitivo desse valor é: {0}'.format(type(p)))
# print('Só tem espaços? {}'.format(p.isspace()))
# print('É número? {}'.format(p.isnumeric()))
# print('É alfabético? {}'.format(p.isalpha()))
# print('É alfanúmerico? {}'.format(p.isalnum()))
# print('Está em maiuscula? {}'.format(p.isupper()))
# print('Está em minúscula? {}'.format(p.islower()))
# print('Está capitalizada? {}'.format(p.isdigit()))

#a partir do python 3.7 pode se utilizar o f antes da frase, conforme abaixo:
print('===========EX004===========')
p = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(p)}')
print(f'Só tem espaços? {p.isspace()}')
print(f'É número? {p.isnumeric()}')
print(f'É alfabético? {p.isalpha()}')
print(f'É alfanúmerico? {p.isalnum()}')
print(f'Está em maiuscula? {p.isupper()}')
print(f'Está em minúscula? {p.islower()}')