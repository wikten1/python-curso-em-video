num = int(input('Digite um número: '))
fat = num
result = 1
resut = result * fat
while fat != 0:
    result = result * fat
    fat -= 1
print(f'O fatorial de {num} é: {result}')