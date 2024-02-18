nome = input('Digite o nome: ').strip()
dividido = nome.split()
print(f'O nome completo é: {nome}\nO primeiro nome é: {dividido[0]}\nO último nome é: {dividido[-1]}')