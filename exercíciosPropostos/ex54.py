from datetime import date
maiores = 0
menores = 0

for i in range(1,8):
    dataNasc = int(input(f'Digite a data de nascimento da {i}° pessoa: '))
    idade = date.today().year - dataNasc
    
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
        
print(f'Das datas de nascimentos digitadas, podemos deduzir que: {maiores} pessoas são maiores de idade e que {menores} pessoas são menores de idade.')    