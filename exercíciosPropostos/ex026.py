frase = input('Digite uma frase: ').strip()
fraseMinu = frase.lower()
qtdA = fraseMinu.count('a')
primeiroA = fraseMinu.find('a')+1
ultimoA = fraseMinu.rfind('a')+1
print(f'A letra "a" aparece: {qtdA}\nAparece na primeira vez no índice: {primeiroA}\n Aparece na última vez no índice: {ultimoA}')