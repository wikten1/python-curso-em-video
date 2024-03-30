classificacaoBrasileirao = ("Flamengo","Palmeiras","Atlético Mineiro",
"São Paulo","Internacional","Fluminense","Grêmio","Athletico Paranaense","Corinthians","Ceará","Fortaleza","Atlético Goianiense","Bahia","Santos","Sport Recife","Juventude","Cuiabá","América Mineiro","Chapecoense","Red Bull Bragantino"
)

print('Os 5 primeiros colocados da tabela são: ')
for i in range(0, 5):
    print(classificacaoBrasileirao[i], end=', ')


print('\n\nOs ultimos 4 colocados da tabela são: ')
for i in range(-5, 0):
    print(classificacaoBrasileirao[i], end=', ')
    
print('\n\nUma lista com os times em ordem alfabetica é: ')
print(sorted(classificacaoBrasileirao))

print(f'\n\nO chapecoence está na posição: {classificacaoBrasileirao.index("Chapecoense")+1}')
