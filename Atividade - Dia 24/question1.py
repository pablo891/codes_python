lista1 = []
lista2 = []
intersecao = []
for contador in range (1, 6):
    addLista1 = int(input('Digite um número para a Lista 1: '))
    lista1.append(addLista1)
    addLista2 = int(input('Digite um número para a Lista 2: '))
    lista2.append(addLista2)

for numero in lista1:
    if numero in lista2 and numero:
        intersecao.append(numero)

for contador in range(len(intersecao)):
    for item in range(contador + 1, len(intersecao)):
        if intersecao[contador] > intersecao[item]:
            intersecao[contador], intersecao[item] = intersecao[item], intersecao[contador]
print(f'Lista de números comuns (Interseção): {intersecao}')