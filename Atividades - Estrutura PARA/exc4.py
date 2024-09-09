number = 0
somaNum = 0
vInicial = int(input('Digite o primeiro valor: '))
vFinal = int(input('Digite o segundo valor: '))

for contador in range(vInicial, vFinal):
    number += vInicial
    somaNum += number
print(f'A soma dos números inteiros desse intervalo é {somaNum}')
