a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

soma = a + b

if soma > c:
    print(f'A soma de {a} + {b} é maior que {c}')
elif soma < c:
    print(f'A soma de {a} + {b} é menor que {c}')
elif soma == c:
    print(f'A soma de {a} + {b} é igual a {c}')