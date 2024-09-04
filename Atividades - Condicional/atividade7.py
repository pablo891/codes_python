valorOriginal = float(input('Qual é o valor original do produto? \nR$'))
formaPag = int(input('Qual a forma de Pagamento?\n[1] Pix, dinheiro ou débito, recebe 15 (%) de desconto\n[2]À vista no cartão de crédito, recebe 10 (%) de desconto \n[3] Em duas vezes, preço normal sem juros \n[4] Em três vezes, preço normal mais juros de 10%\n'))
valor1 = valorOriginal * 0.85
valor2 = valorOriginal * 0.9
valor3 = valorOriginal / 2
valor4 = valorOriginal * 1.1
div4 = valor4 / 3

if formaPag == 1:
    print(f'O valor do produto final é: \nR${valor1:.2f}')
elif formaPag == 2:
    print(f'O valor do produto final é: \nR${valor2:.2f} em 1x no cartão de crédito')
elif formaPag == 3:
    print(f'O valor do produto final é: \nR${valorOriginal:.2f}, divido em 2 vezes de R${valor3:.2f} ')
elif formaPag == 4:
    print(f'O valor do produto final é: \nR${valor4:.2f}, dividido em 3 vezes de R${div4:.2f}')