n = int(input('Digite um número:'))
divisor= 0

for contador in range(1, n):
    if contador % n == 0:
        divisor += contador
    
if divisor == n:
    print(f'O número {n} é perfeito')
    
else:
    print(f'O número {n} não é perfeito')
    

    