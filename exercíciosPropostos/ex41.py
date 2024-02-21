anoNasc = int(input('Digite o ano de nascimento do atleta: '))

if anoNasc <= 9:
    print('Categoria: Mirim')
elif anoNasc > 9 and anoNasc <= 14:
    print('Categiria: Infantil')
elif anoNasc > 14 and anoNasc <= 19:
    print('Categoria: Junior')
elif anoNasc > 19 and anoNasc <= 20:
    print('Categoria: Senior')
else:
    print('Categoria: Master')
    