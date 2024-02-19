velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print(f'O carro foi multado em R${multa}!')
else:
    print('O carro não foi multado!')
    