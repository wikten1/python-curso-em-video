frase = input('Digite uma frase: ').strip().lower()
lista = frase.split()
semEspaco = ''.join(lista)
inverso = ''

for i in range(len(semEspaco)-1, -1, -1):
    inverso += semEspaco[i]
if inverso == semEspaco:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')

