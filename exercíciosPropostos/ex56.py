somaIdades = 0
hMaisVelho = 0
maisNovas = 0

for i in range(1,5):
    nome = input(f'Digite o nome da {i}° pessoa: ').strip()
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    sexo = input(f'Digite o sexo da {i}° pessoa (M/F): ').upper()[0]
    
    somaIdades += idade
    
    if sexo == 'M':
        if idade > hMaisVelho:
            hMaisVelho = idade
    
    if sexo == 'F':
        if idade < 20:
            maisNovas += 1
            
media = somaIdades/4

print(f'A média da idade das pessoas é: {media}')
print(f'A idade do homem mais velho é: {hMaisVelho}')
print(f'A quantidade de mulheres menores de 20 anos é: {maisNovas}')