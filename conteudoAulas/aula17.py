'''
num = [2,5,9,1]
num[2]= 3
num.append(6) #adiciona o elemento no fim da lista
num.sort() #Organiza os elementos por ordem numérica ou alfabética
num.sort(reverse=True) #Organiza os elementos por ordem numérica decressente ou alfabética contraria
num.insert(2,0) #insere o número (0) na posição (2)
num.pop(2) # Remove o último valor da lista se as aspas estiverem vazias ou o do índice procurado se tiver preenchido
del num[3] #remove o valor procurado da lista
num.remove(2) #Remove a primeira ocorrencia do valor procurado na lista
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Retorna quantos elementos a lista possui
'''

'''
valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')
    
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei {v}!')
print('Cheguei ao final da lista.')
'''

a = [2,3,4,6]
b = a[:] #Copia todos os valores de a para b e não cria uma ligação entre as listas.
b[2]= 8

print(f'Lista A:{a}')
print(f'Lista B:{b}')