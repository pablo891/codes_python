pos = 0
neg = 0

for contador in range(1,9):
    num = int(input('Digite um número: '))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print(f'Quantidade de positivos: {pos}')
print(f'Quantidade de negativos: {neg}') 
