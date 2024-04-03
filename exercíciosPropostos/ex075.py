n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))
pares = 0

tupla = (n1, n2, n3, n4)

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado no indice {tupla.index(3)}')
else:
    print("O valor 3 não foi digitado")
print(f'Os números pares da tupla são: ')
for i in tupla:
    if i % 2 == 0:
        pares += 1
        print(i, end=' ')
    
if pares == 0:
    print('Não há números pares.')
    