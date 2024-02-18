nome = input('Digite o seu nome completo: ')
semEspaço = nome.split()
nomeJunto = ''.join(semEspaço)
print(f'O nome completo da pessoa em maiúsculo é: {nome.upper()}\n O nome completo da pessoa em minúsculas é: {nome.lower()}\nA quantidade de letras do nome todo é: {len(nomeJunto)}\nA quantidade de letreas do primeiro nome é: {len(semEspaço[0])} ')