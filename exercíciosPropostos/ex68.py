from random import randint

num = soma = tentativa = 0
while True:
    escolha = input('Digite "impar" ou "par": ').lower()
    
    num = int(input("Digite um número entre 1 e 10: "))
    respComp = randint(1,100)
    result = num + respComp
    
    if result % 2 == 0:
        if escolha == "par":
            print(f'Parabéns você ganhou!')
            print(f'O número de tentativas foi{tentativa}')
            break
        else:
            print("Você perdeu!")
            tentativa += 1
    elif result % 2 != 0:
        if escolha == "impar":
            print(f'Parabéns você ganhou!')
            print(f'O número de tentativas foi{tentativa}')
            break
        else:
            print("Você perdeu!")
            tentativa += 1
    else:
        print("Opção inválida, tente novamente!")
        tentativa -= 1

    
    