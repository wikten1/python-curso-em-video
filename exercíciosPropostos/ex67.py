while True:
    num = int(input('Digite um número: '))
    if num >=0:
        for i in range(1, 11, 1):
            print(f'{num} X {i} = {num*i}')
    else:
        break
            
            
            