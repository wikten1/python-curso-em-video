valor = int(input("Digite quanto quer sacar: "))
tot = valor

cedula = 50
totCedula = 0
while True:
    if tot >= cedula:
        tot -= cedula
        totCedula += 1
    else: 
        if totCedula > 0:
            print(f'Total de {totCedula} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if tot == 0:
            break

print("Obrigado por escolher o banco Wikbank e volte sempre.")