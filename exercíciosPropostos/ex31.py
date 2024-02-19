distancia = int(input('Digite a distância da viagem em KMs: '))
if distancia < 200:
    print(f'O valor da passagem será: R${distancia*0.5}')
else:
    print(f'O calor da passagem será: R${distancia*0.45}')