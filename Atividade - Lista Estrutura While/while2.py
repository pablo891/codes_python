import datetime 
data = datetime.datetime.now()
ano = data.year
acesso = 0

while True:

    anoNascimento = int(input("Informe o ano do seu nascimento: "))

    acesso = ano - anoNascimento 
    if acesso >= 18:
        print("Você pode se inscrever no concurso!")
        break
