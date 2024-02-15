qtdKm = float(input('Qual a quantidade de KMs percorridos: '))
diasAluguel = int(input('Quantos dias foi alugado: '))
total = qtdKm*0.15 + 60*diasAluguel
print(f'O valor total do carro alugado foi de: R${total:.2f}')