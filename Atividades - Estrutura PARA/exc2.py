somaAge = 0
totalPessoas = 0

for contador in range(1,6):
    age = float(input('Digite sua idade: '))
    if age >= 18:
        totalPessoas += contador
        print(f'Total de pessoas maiores de idade: {totalPessoas}')