media = 33.5
sameMedia = 0
acimaMedia = 0
abaixoMedia = 0
for contador in range(1,8):
    temp = float(input('Digite a temperatura: '))
    if temp == media :
        sameMedia += 1
    elif temp > media :
        acimaMedia += 1
    else:
        abaixoMedia += 1

print(f'Temperaturas iguais à Média: {sameMedia}')
print(f'Temperaturas acima da Média: {acimaMedia}')
print(f'Temperaturas abaixo da Média: {abaixoMedia}')