soma = 0 # estamos inicializando variável com o valor zero

totalPares = 0 # será responsável por contar todos os valores pares

for contador in range(50,71):
    if contador % 2 == 0:
        soma = soma + contador # soma += contador
        totalPares += 1

print(f'A soma dos valores pares é {soma}')
print(f'A média dos pares é {soma / totalPares}')
print(f'O total de valores pares é {totalPares}')