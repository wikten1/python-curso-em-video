soma = 0
num = 0
cont = 0
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
print(f'A soma dos {cont-1} números é: {soma}')