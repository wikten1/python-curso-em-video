'''
for c in range(1,10):
    print(c)
print('Fim!')
'''

'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim!')
'''

'''
for c in range(1,5):
    n = int(('Digite um valor: '))
print('Fim!')
'''
'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')
'''

'''
resp = 's'
while resp == 's':
    n = int(input('Digite um valor: '))
    resp = input('Quer continuar?: ').lower()
print('Fim!')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        
print(f'Você digitou {par} números pares e {impar} números impares!')


