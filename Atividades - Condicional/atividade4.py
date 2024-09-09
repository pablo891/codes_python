valor = int(input('Digite um valor: ')) 

if valor%2 == 0:
    soma = valor +10
    print(f'Resultado da soma: {soma}')
elif valor%2 != 1:
    mult = valor * 2
    print(f'Resultado da multiplicação: {mult}')