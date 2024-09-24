import random
moeda = ['Cara', 'Coroa']
listaResultados = []

while True:
    lancamento = random.choice(moeda)
    print(f'O resultado do lançamento da moeda foi: {lancamento}')
    listaResultados.append(lancamento)
    
    jogarNovamente = int(input('Deseja continuar o lançamento? [1] Sim [2] Não\n'))
    
    if jogarNovamente == 2:
        print(f'Resultado das sequências de lançamento: {listaResultados}')
        break