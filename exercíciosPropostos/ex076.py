tupla = ("Lápis", 1.50, "Caderno", 30.00, "Borracha", 0.50, "Caneta", 3.20, "Liquipaper", 5.30)

print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end=' ')
    else:
        print(f'{tupla[pos]:>7.2f}')

