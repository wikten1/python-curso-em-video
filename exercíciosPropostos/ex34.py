salario = float(input('Digite o salário: '))
if salario > 1250:
    print(f'O novo salário do funcionário será R${salario + (salario*10/100):.2f}')
else:
    print(f'O novo salário do funcionário será R${salario + (salario*15/100):.2f}')