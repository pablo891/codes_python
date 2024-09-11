valorA = int (input ("Informe o valor de A: "))
valorB = int (input ("Informe o valor de B: ")) 
multiplos = 0
naoMultiplos = 0

for contador in range(valorA,valorB):
    if valorA % 7 == 0 and valorB % 11 == 0:
        multiplos += 1

else:
     naoMultiplos +=1
     
print(f"O total de multiplos é {multiplos}")
print(f"O total não multiplos é {naoMultiplos}")
    