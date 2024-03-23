maior18 = qtdHomens = qtdMulherMenor20 = 0
contador = 1
resp = 'S'
while resp == 'S':
    idade = int(input(f"Digite a idade da {contador}ª pessoa: "))
    sexo = input("Digite o sexo da ('M' ou 'F'): ").upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        qtdMulherMenor20  += 1
    contador += 1
    resp = input("Deseja continuar (S/N): ").upper()[0]
    
    
print(f"A quantidade de pessoas maiores de 18 anos é: {maior18}")
print(f"A quantidade de Homens é: {qtdHomens}")
print(f"A quantidade de mulheres menores de 20 anos é: {qtdMulherMenor20}")