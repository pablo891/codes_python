meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
media = 0
somaTemp = 0
acimaMedia = []
contador = 0

for itens in meses:
    temp = int(input('Digite a temperatura média do mês: '))
    somaTemp += temp 
    temperaturas.append(temp)

media = somaTemp / 12
print(f'Média das temperaturas: {media:.2f} ºC')

for indice, itens in enumerate (temperaturas):
    if itens > media:
        acimaMedia.append(itens)
        print(f'{indice}º mês: {meses[indice]} e a temperatura foi {itens} ºC ')
