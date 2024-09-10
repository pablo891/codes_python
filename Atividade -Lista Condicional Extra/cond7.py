# Declaração das variáveis
nota = float(input('Digite a nota do aluno: '))
frequencia = int(input('Digite a frequência do aluno (em porcentagem): '))

# Aplicando condicionais de aprovação
if nota >= 7 and frequencia >= 75 :
    print(f'SITUAÇÃO: O aluno está aprovado!')
else: 
    print('SITUAÇÃO: O aluno está reprovado!')
