import random

tentativas = 3
frutas = ['maçã', 'banana', 'laranja', 'morango', 'uva', 'abacaxi', 'kiwi', 'manga', 'pera', 'melancia', 'framboesa', 'nectarina', 'carambola', 'figo', 'amora']

print(f'Lista Original: {frutas}')
random.shuffle(frutas)
print('-' * 60)

palavraEscolhida = random.choice(frutas)

posicaoCorreta = frutas.index(palavraEscolhida)

print("Bem-vindo ao jogo! Você terá que adivinhar a posição de uma palavra na lista embaralhada.")
print("A lista possui 15 palavras, e as posições vão de 0 a 14.")

while tentativas > 0:
    palpite = int(input(f"A palavra escolhida é: '{palavraEscolhida}'. Em qual posição (0 a 14) você acha que ela está?\n "))
    
    if palpite == posicaoCorreta:
        print("Parabéns! Você acertou!\n")
        break
    else:
        tentativas -= 1
        print(f"Você errou! Tentativas restantes: {tentativas}\n")

if tentativas == 0:
    print(f"Você esgotou suas tentativas. A palavra '{palavraEscolhida}' estava na posição {posicaoCorreta}\n")

print("Aqui está a lista embaralhada:")
print(frutas)
