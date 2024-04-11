lista = []
maior = 0
menor = 0
for i in range(0,5):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))
    if i == 0:
        menor = lista[i]
    else:
        if menor > lista[i]:
            menor = lista[i]
    
    if maior < lista[i]:
        maior = lista[i]

print(f"O maior valor da lista é: {maior} e sua posição na lista é {lista.index(maior)+1}")
print(f"\nO menor valor da lista é: {menor} e sua posição na lista é {lista.index(menor)+1}")
