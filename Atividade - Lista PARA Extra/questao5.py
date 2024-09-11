import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
sorteado = 0

print('Bem-vindo ao Lançamento de Dados! \n')
for contador in range(1, 11):
    sorteado = random.randint(1, 7)
    print(f'Número sorteado: {sorteado}')

    if sorteado == 1:
        num1 += 1
    elif sorteado == 2:
        num2 += 1
    elif sorteado == 3:
        num3 += 1
    elif sorteado == 4:
        num4 += 1
    elif sorteado == 5:
        num5 += 1
    elif sorteado == 6:
        num6 += 1

print(f'Quantidade de número 1: {num1}')
print(f'Quantidade de número 2: {num2}')
print(f'Quantidade de número 3: {num3}')
print(f'Quantidade de número 4: {num4}')
print(f'Quantidade de número 5: {num5}')
print(f'Quantidade de número 6: {num6}')