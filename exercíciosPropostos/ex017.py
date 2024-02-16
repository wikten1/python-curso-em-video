import math
catOP = float(input('Digite a medida do cateto oposto: '))
catAD = float(input('Digite a medida do cateto adjacente: '))
print(f'A hipotenusa do triângulo retângulo procurado é: {math.hypot(catOP,catAD):.2f}')