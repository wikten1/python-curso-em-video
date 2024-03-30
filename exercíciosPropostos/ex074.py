from random import randint

tupla = (randint(1,100), randint(1,100), randint(1,100), randint(1,100),randint(1,100))

maior = 0
menor = 0
cont = 1

for i in tupla:
    if i > maior:
        maior = i
    
    if cont == 1:
        menor = i
    else:
        if menor > i:
            menor = i
    
print(f'A listagem do número gerado é: {tupla}')        
print(f'O maior elemento da tupla é: {maior}')
print(f'O menor item da tupla é: {menor}')

