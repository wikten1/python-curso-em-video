'''
teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['João', 19], ['Maria', 22], ['Joaquin', 12], ['Ana', 40]]
print(galera)
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dado = list()
totalmai = totalmen = 0

for c in range(0, 5):
    dado.append(input('Nome: '))
    dado.append(int(input("idade: ")))
    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmen += 1
        
print(f'Temos {totalmai} maiores e {totalmen} menores de idade.')
