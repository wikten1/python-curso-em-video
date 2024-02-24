'''
for c in range(1,6):
    print('oi')
print('fim')
'''

#crescente
'''
for c in range(1,6):
    print(c)
print('fim')
'''

#decrescente
'''
for c in range(6,0,-1):
    print(c)
print('fim')
'''

#De dois em dois
'''
for c in range(0, 7, 2):
    print(c)
print('fim')
'''

#Determinando o número final
'''
n = int(input('Digite um número inteiro: '))

for c in range(0, n):
    print(c+1)
print('Fim!')
'''

#Determinando tudo
'''
inicio = int(input('Digite o número de início: '))
fim = int(input('Digite o número de fim: '))
passo = int(input('Digite o passo: '))

for c in range(inicio, fim, passo):
    print(c)
print('Fim!')
'''

#Repetição de comandos com números determinados
s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print(f'O somatório dos números é: {s}')
print('FIM!')
