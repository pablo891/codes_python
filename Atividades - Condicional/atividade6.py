a = int(input('Insira o valor A: '))
b = int(input('Insira o valor B: '))
c = int(input('Insira o valor C: '))

if a < b and b < c:
    print(f'Forma Ascendente: {a}, {b} e {c}')
elif a > b and b > c:
    print(f'Forma Ascendente: {c}, {b} e {a}')
elif a > b and b < c and a > c:
    print(f'Forma Ascendente: {b}, {c} e {a}')