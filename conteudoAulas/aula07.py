#5+3*2

#5**2

#5**3

#19//2

#19/2

#365*522

#18%2

#122%3

#4**3

#pow(4,3)

#81**(1/2)

#25**(1/2)

#127**(1/3)

#'oi' + 'Olá'

#'oi' * 5

#'='*20

#print('='*20)

'''
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:20}!')
'''

'''
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:>20}!')
'''

'''
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:<20}!')
'''

'''
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:^20}!')
'''

'''
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:=^20}!')
'''

n1 = int(input('Um valor: '))

n2 = int(input('outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {}, o produto é {}\n e a divisão é {:.3f}'.format(s,m,d), end=' ')

print('Divisãi inteira {} e potência {}'.format(di, e))