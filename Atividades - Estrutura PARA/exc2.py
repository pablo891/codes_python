somaAge = 0
totalPessoas = 0

for contador in range(1,6):
    age = float(input('Digite sua idade: '))
    somaAge += age
    totalPessoas += 1
print(f'A  média de idade das pessoas é {somaAge / totalPessoas} anos')