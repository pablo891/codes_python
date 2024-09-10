#  Declaração de variáveis 
compra = float(input('Digite o valor do produto: ')) 
parcela = int(input('Digite a quantidade de parcelas desejadas (1x à 24x): '))
vParcela = 0

# Aplicando as condicionais de parcela
if parcela > 12 :
    vParcela = (1.015 * compra + 6) / parcela
    print(f'Valor das parcelas: R$ {vParcela:.2f}')
