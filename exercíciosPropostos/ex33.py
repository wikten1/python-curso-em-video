n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))

if n2 >= n1:
    if n2 >= n3:
        print('O maior número é o N2!')
    else:
        print('O maior número é o N3!')
else:
    if n1 >= n3:
        print('O maior número é N1!')
    else:
        print('O maior número é o N3!')