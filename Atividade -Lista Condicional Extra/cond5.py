horas = int(input("Digite a quantidade de horas trabalhadas: "))
valorHora= float(input("Digite o valor por hora: "))
horasNormal= 40
salario = 00
       
if horas > horasNormal:  # Verificar se as horas trabalhadas são superiores ao limite
    totalExtra = 1.5 * valorHora * horas
    salario = totalExtra  
    print(f"O salário total com horas extras é: R$ {salario}")

else:
 # Se não houver horas extras, o salário é apenas o das horas normais
    totalExtra = valorHora * horas
    salario = totalExtra
    print(f'O salário total é {salario}')
