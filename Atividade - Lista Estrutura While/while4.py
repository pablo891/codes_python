print('Bem-vindo ao lojão do Manoel!')

contador = 0
totalCompra = 0
troco = 0
pagamento = 0

while True:
    contador += 1
    valorProduto = float(input(f'Digite o valor do produto: R$'))
    totalCompra += valorProduto
    
    if valorProduto == 0:

        print(f'Total da compra: R${totalCompra:.2f}\n')

        pagamento = float(input('Informe a quantia em dinheiro de pagamento: \n'))
        troco = pagamento - totalCompra

        print(f'Dinheiro: R${pagamento:.2f}\n')
        print(f'Troco: R${troco:.2f}\n')
        break
    
