precoProd = float(input('Digite o preço do produto: '))
condPag = int(input('''Digite a condição de pagamento
                      (Dinheiro/check = 1)
                      (Cartão 1x = 2)
                      (Cartão 2x = 3)
                      (3x ou mais = 4): '''))

if condPag == 1:
    print(f'O valor do produto é {precoProd - (precoProd*10/100)}')
elif condPag == 2:
    print(f'O valor do produto é {precoProd - (precoProd*5/100)}')
elif condPag == 3:
    print(f'O valor do produto é {precoProd}')
else:
    print(f'O valor do produto é: {precoProd + (precoProd*20/100)}')



