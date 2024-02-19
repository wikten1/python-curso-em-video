import random
num = int(input('Digite um número de 1 a 5: '))
numRandon = random.randint(1,5)
if num == numRandon:
    print('Parabéns você venceu!')
else:
    print('O computador venceu!')
print('Game over!')
