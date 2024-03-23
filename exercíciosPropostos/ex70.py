maisBarato = 0
nomeMaisBarato = ''
maiorQueMil = soma = 0
resp = 'S'
cont = 1

while resp == 'S':
    valor = int(input(f'Digite o valor do {cont}º produto: '))
    nomeProd = input('Digite o nome do produto: ')
    if maisBarato == 0:
        maisBarato = valor
        nomeMaisBarato = nomeProd
        
    if maisBarato > valor:
        maisBarato = valor
        nomeMaisBarato = nomeProd
    
    
    if valor > 1000:
        maiorQueMil += 1
        
    soma += valor
    cont += 1
    
    resp = input("Deseja contiar (S/N): ")
    
print(f"O total da compra é: {soma}")

print(f"O nome do produto mais barato é: {nomeMaisBarato}")

print(f'A quantidade de produtos maior que mil reais: {soma}')
    
    
