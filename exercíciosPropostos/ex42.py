r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento sa terceira reta: '))

if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('As retas definidas conseguem formar um triângulo: ')
    if r1 == r2 and r2 == r3:
        print('O triângulo é um triângulo Equilátero!')
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r1 != r2) or (r3 == r1 and r2 != r1):
        print('O triângulo é Isósceles!')
    else:
        print('O triângulo é Escaleno!')
else:
    print('As retas definidas não conseguem formar um triângulo: ')