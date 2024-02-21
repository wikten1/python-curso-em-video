import datetime
sexo = input('Digite o seu sexo (M - masculino) ou (F - feminino): ').upper()
anoNasc = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - anoNasc
if sexo == 'M':
    if idade < 18:
        print(f'Faltam {18-idade} anos para poder se alistar!')
    elif idade == 18:
        print(f'Já está na hora de se alistar!')
    else:
        print(f'Já passaram {idade-18} anos da data de alistamento!')
elif sexo == 'F':
    print('Alistamento não obrigatório.')
else:
    print('Opção invaslida! Tente novamente.')