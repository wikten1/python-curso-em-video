maiorPeso = 0
menorPeso = 1000

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    
    if peso > maiorPeso:
        maiorPeso = peso
        
    if peso < menorPeso:
        menorPeso = peso

print(f'O maior peso registrado foi: {maiorPeso:.2f}')
print(f'O menor peso registrado foi: {menorPeso:.2f}')