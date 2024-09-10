salario = float(input('Digite seu salário: '))

# Aplicação das condicionais de Imposto de Renda
if salario <= '1900' :
    print('Imposto de Renda: R$ 0,00')

if salario > 1900 and salario <= 2800 :
    imposto = 0.075 * salario
    print(f'Imposto de Renda: {imposto:.3f}')

if salario > 2800 and salario <= 3700 :
    imposto = 0.15 * salario
    print(f'Imposto de Renda: {imposto:.3f}')

if salario > 3700  :
    imposto = 0.225 * salario
    print(f'Imposto de Renda: {imposto:.3f} ')


