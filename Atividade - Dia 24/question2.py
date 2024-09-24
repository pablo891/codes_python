notas = []
media = 7
alunosMedia =0

while True:
    nota = float(input("Digite a nota do aluno: "))   
    notas.append(nota)
    for itens in notas:
        if itens > media:
            alunosMedia += 1
    print(f"Quantidade de alunos com notas acima da média: {alunosMedia} alunos")


    if nota == 0:
        break

