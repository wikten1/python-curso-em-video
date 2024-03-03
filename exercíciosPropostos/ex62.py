termo1 = int(input('Digite o primeiro termo da sequência: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
total = 0
mais = 10
print('Os 10 primeiros termo da PA são: ')
print(termo1)
while mais != 0:  
    total = total + mais
    while cont != total:
        termo1 = termo1 + razao
        print(termo1)
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais ?: '))
print('Fim!')
