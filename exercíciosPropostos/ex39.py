import datetime
anoNasc = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - anoNasc

if idade < 18:
    print(f'Faltam {18-idade} anos para poder se alistar!')
elif idade == 18:
    print(f'Já está na hora de se alistar!')
else:
    print(f'Já passaram {idade-18} anos da data de alistamento!')