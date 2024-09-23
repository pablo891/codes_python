valorConta = float(input('Digite o valor da conta a ser pago: R$'))
gorjeta = int(input('Qual o percentual de gorjeta que você deseja dar (em porcentagem): '))
gorjetaTotal = 0
total = 0

gorjetaTotal = (gorjeta * valorConta) / 100
total = valorConta + gorjetaTotal

print(f'Gorjeta: R${gorjetaTotal:.2f}')
print(f'Total: R${total:.2f}')