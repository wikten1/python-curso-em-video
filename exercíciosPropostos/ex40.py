nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1} e {nota2} tem a média {media} ')
if media < 5:
    print('Aluno está Reprovado!')
elif media > 5 and media <= 6.9:
    print('Aluno está Recuperação!')
else:
    print('Aluno está Aprovado!')