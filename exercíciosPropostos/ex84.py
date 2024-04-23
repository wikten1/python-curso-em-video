temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
            
    princ.append(temp[:])
    temp.clear()
    resp = input("Digite S para continuar e N para sair: ")
    
    if resp in 'Nn':
        break

print(f'Os dados foram: {princ}')
print(f'Ao todo você tem {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {maior}KG.')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {menor}KG.')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
    