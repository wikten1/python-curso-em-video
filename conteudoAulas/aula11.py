#print('\033[1;31;43mOlá, Mundo\033[m')
#print('\033[4;30;45mOlá, Mundo\033[m')

'''
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m ')
'''

'''
nome = 'Wikten'
print(f'Olá! Muito prazer em te conhecer, {'\033[4;34m'}{nome}{'\033[m'}')
'''

nome = 'Wikten'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}

print(f'Olá! Muito prazer em te conhecer, {cores["pretobranco"]}{nome}{cores["limpa"]}')