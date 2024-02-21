import random
escolha = input('Digite uma das seguinte escolhas (pedra, papel, tesoura): ').lower()

lista = ['pedra', 'papel', 'tesoura']
escolhaPc = random.choice(lista)

if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura':
    if escolha == 'pedra':
        if escolhaPc == 'pedra':
            print('Empate!')
        elif escolhaPc == 'papel':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
    elif escolha == 'papel':
        if escolhaPc == 'papel':
            print('Empate!')
        elif escolhaPc == 'tesoura':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
    else:
        if escolhaPc == 'tesoura':
            print('Empate!')
        elif escolhaPc == 'pedra':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
else:
    print('Opção invalida! Tente novamente.')
    