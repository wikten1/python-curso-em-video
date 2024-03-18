num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e a soma dos números é: {soma}')
