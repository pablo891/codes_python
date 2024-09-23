import random
jogarNovamente = 'sim'

while jogarNovamente == 'sim':

    print("Escolha: 1:Pedra/ 2:Papel/ 3:Tesoura ")
    usuario = int(input("Digite sua escolha (1, 2 ou 3): "))

    computador = random.randint(1, 3) #escolha do computado0r

    escolha = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    print(f"Você escolheu: {escolha[usuario]}")
    print(f"O computador escolheu: {escolha[computador]}")

    if usuario == computador:
        resultado = "Empate!"
    elif (usuario == 1 and computador == 3) or \
         (usuario == 2 and computador == 1) or \
         (usuario == 3 and computador == 2):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    print(resultado)
