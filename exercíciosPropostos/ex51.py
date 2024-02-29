termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo1 + (10-1) * razao
for i in range(termo1,decimo+1, razao):
    print(i + termo1)

