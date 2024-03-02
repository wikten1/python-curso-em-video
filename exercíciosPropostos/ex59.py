escolha = 6
while escolha != 5:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    escolha = int(input('''Escolha uma das seguintes opções
                        [1]somar
                        [2]multipicar
                        [3]maior
                        [4]novos números
                        [5]sair do programa: '''))
    
    if escolha == 1:
        print(f'A soma dos números digitados é: {n1 + n2}')
    
    if escolha == 2:
        print(f'A multiplicação dos números digitados é: {n1*n2}')
    
    if escolha == 3:
        if n1 >= n2:
            print(f'O primeiro número digitado {n1} é maior!')
        else:
            print(f'O segundo número digitado {n2} é maior!')
    
    if escolha > 5:
        print('Opção inválida, tente novamente!')
print('Fim!')