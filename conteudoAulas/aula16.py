#As tuplas são imutaveis
#As tuplas usam parenteses na sua declaração

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
'''
print(lanche)
'''
#Mostra o lanche de indice 1
'''
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
'''

'''
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
'''

#ou

'''
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {cont}')
print('Comi pra caramba!')
'''

'''
for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont}')
print('Comi pra caramba!')
'''

'''
print(sorted(lanche)) #printa a tupla de forma ordenada
'''
'''
a = (2, 5, 4)

b = (5, 8 ,1 ,2)

c = b+a #Soma de tuplas

print(c)
print(len(c)) #mosra a quantidade de elementos de uma tupla
print(c.count(5)) #Conta quantas vezes o número 5 aparece dentro da tupla
print(c.index(8)) #Exibe o indice do primeiro número 8 da tupla
print(c.index(5, 1)) #Procura o indice do primeiro número 5 apartir do indice de posição 1
'''

pessoa = ('Wikten', 24, 'M', 68.5) #As tuplas diferetemente dos vetores de outras linguagens aceitam valores de tipos diferentes.
print(pessoa)
del(pessoa) #apaga completamente a lista da memoria. Obs(não da para apagar apenas um elemento da tupla separadamente.)
print(pessoa) 