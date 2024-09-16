valor = int(input('Informe o valor numérico: '))

if valor >= 20:
    print(f'O número {valor} é maior ou igual a 20\n')

# ELSE IF 
elif valor >= 10 and valor <= 20:
    print(f'O número {valor} está entre 10 e 20\n')

else:
    print(f'O número {valor} é menor que 20\n')
