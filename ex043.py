# Exercicio 43

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu satus, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('='*11,'ex043','='*11)
peso = float(input('Qual o seu peso: (kg) '))
altura = float(input('Qual a sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.0f}'.format(imc))
if imc < 18.5:
    print('Abaixo de 18.5: Abaixo do peso')
elif imc >= 18.5 and imc <= 24:
    print('Entre 18.5 e 24: peso ideal')
elif imc >= 25 and imc <= 29:
    print('25 até 29: Sobrepeso')
elif imc >= 30 and imc <= 34:
    print('30 até 34: Obesidade')
elif imc >= 35 and imc <= 40:
    print('35 até 40: Obesidade Grau 2')
else:
    print('Acima de 40: Obesidade mórbida')