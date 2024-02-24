s = 0
for i in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n%2==0:
        s += n
print(f'A soma dos números pares digitados foi: {s}')
print('Fim!')