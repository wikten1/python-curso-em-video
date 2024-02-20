valCasa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos deseja pagar: '))

prestacao = valCasa/(anos*12)

if prestacao < (sal*30/100):
    print('Parabéns, sua compra foi aprovada!')
else:
    print('Sinto muito, mas a compra não será possível!')
    
    