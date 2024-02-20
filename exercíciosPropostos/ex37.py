num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[1] Converter para BINÁRIO
[2]Converter para OCTAL
[3]Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} Convertido para BINARIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Erro! Escolha uma das opções validas.')