valores = []

while True:
    numero = int(input('Digite um valor: '))

    if numero <= 0:
        break
    valores.append(numero)
print(valores)

for contador in valores:
    if contador % 2 == 0:
        valores.remove(contador)
print(valores)