peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de: {imc}')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')