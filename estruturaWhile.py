# 1ª forma de utilizar while - semelhante ao FOR
contador = 1

while contador <= 5:
    contador += 1
    print('contador')

# 2ª forma de utilizar while - loop condicional normal
valor  = 0

while valor == 0:
    valor = int(input('Informe um valor qualquer (Digite um valor para terminar): '))

    print(f'Você digitou {valor}')

# 3ª forma de utilizar o while - semelhante a estrutura faça enquanto
while True:
    senha = input('Informe sua senha: ')

    if senha == '123':
        print('Parabéns, senha correta')
        break # forma de encerrar o loop
    else:
        print('Senhas não conferem, tente novamente')