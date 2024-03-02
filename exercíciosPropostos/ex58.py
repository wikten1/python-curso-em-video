from random import randint
aleatorio = randint(1,10)
n = 11
cont = 0
while n != aleatorio:
    n = int(input('Digite um número entre 1 e 10: '))
    aleatorio = randint(1,10)
    cont += 1

print(f'Parabéns você acertou!\nO número de tentativas foi {cont}')
    