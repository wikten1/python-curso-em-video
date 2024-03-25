#As tuplas são imutaveis
#As tuplas usam parenteses na sua declaração

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
#Mostra o lanche de indice 1
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])

'''
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

#ou

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {cont}')
print('Comi pra caramba!')

for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont}')
print('Comi pra caramba!')