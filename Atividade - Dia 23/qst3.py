import time
numeroSegundos = int(input("Informe um número de segundos para a contagem regressiva: "))

for i in range(numeroSegundos, 0, -1):
    print(i)
    time.sleep(1)  

print("Tempo esgotado!")


