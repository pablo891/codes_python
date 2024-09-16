import random

contador = 5

while contador >= 1:
    numAleatorio = random.randint (1,101)
    contador -= 1
    numUser = int(input('Tente adivinhar o número secreto ( 1 a 100): '))

    if numUser == numAleatorio:
        print('O número informado é igual ao número secreto!')
        break

    elif numUser > numAleatorio:
        print('O número informado é maior que o número secreto!')
    
    elif numUser < numAleatorio:
        print('O número informado é menor que o número secreto!')
    print(f'Total de tentativas restantes: {contador} \n')

    if contador < 1:
        print('Você não tem mais tentativas :/')
        print(f'O número secreto era: {numAleatorio}')
        break

