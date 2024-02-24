s = 0
for i in range(1, 501, 2):
    if i%3==0:
        s += i
print(f'A soma dos números impares entre 1 e 500 que são multiplos de três é: {s}')
print('Fim!')