lista = []
resp = 's'
cont = 0
while True:
    if cont == 0:
        lista.append(int(input(f'Digite o {cont+1}º número:')))
    else:
        num =  int(input(f'Digite o {cont+1}º número:'))
        if num not in lista:
            lista.append(num)
            
    
    resp = input('Digite (S) para continuar e (N) para sair: ').lower().strip()
    if resp == 'n':
        break
    cont += 1

lista.sort()
print(f'A lista em ordem crescente é: {lista}')