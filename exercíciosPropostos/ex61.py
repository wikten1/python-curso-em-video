termo1 = int(input('Digite o primeiro termo da sequência: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
print('Os 10 primeiros termo da PA são: ')
print(termo1)
while cont != 10:
    termo1 = termo1 + razao
    print(termo1)
    cont += 1
