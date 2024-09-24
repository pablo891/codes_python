eventos = ["0.Reunião com equipe" , "1.Almoço com cliente" , "3.Consulta médica"]

print("Os eventos agendados para o mês: ")
for itens in eventos:
    print(itens)

print("-"*50)
 
opções =  int(input("Escolha uma opção: [1] Adicionar um novo evento [2] Remover um evento [3] Sair: "))

if opções == 1:
    eventoNovo =  input("Informe o evento que você quer adcionar:")
    eventos.append(eventoNovo) 

print("-"*50)

print(eventos)

if opções == 2:
    posicao = int(input("Informe a posição do evento (0-2): "))
    eventos.pop(posicao) 
    print(eventos)

if opções == 3:
    print(f"A sua lista de eventos para a semana é: {eventos}")

