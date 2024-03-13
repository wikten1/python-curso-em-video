soma = 0
resp = 'S'
maior = 0
menor = 99999999
cont = 0
while resp != 'N':
    num = int(input('Digite um número: '))
    soma += num
    
    if num > maior:
        maior = num
    
    if menor > num:
        menor = num
        
    cont += 1
    resp = input('Deseja continuar [S/N]: ').upper()[0]
    
print(f'A soma dos {cont} números é: {soma}')
print(f'O maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
print(f'A média dos números digitados é: {soma/cont:.2f}')
