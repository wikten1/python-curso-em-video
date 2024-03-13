soma = 0
resp = 'S'
cont = 0
while resp != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    resp = input('Deseja continuar [S/N]: ').upper()[0]
print(f'A soma dos {cont} números é: {soma}')