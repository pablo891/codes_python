atividade = int(input('Qual foi a atividade física realizada\n[1] Caminhada\n[2] Corrida\n[3] Ciclismo\n'))
tempo = int(input('Digite o tempo de realização (em minutos): '))
calorias = 0

if atividade == 1:
    calorias = 5 * tempo
    print(f'Quantidade de calorias queimadas com Corrida: {calorias} kCal')

elif atividade == 2:
    calorias = 10 * tempo
    print(f'Quantidade de calorias queimadas com Corrida: {calorias} kCal')

elif atividade == 3:
    calorias = 8 * tempo
    print(f'Quantidade de calorias queimadas com Ciclismo: {calorias} kCal')