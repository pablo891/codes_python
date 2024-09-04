nome = input('Informe seu nome: ')
sexo = input('Informe seu sexo (F ou M): ')
estadoCivil = input('Informe seu estado civil: ')

if sexo == 'F' and estadoCivil == 'CASADA':
    tempo = input('Quanto tempo de casada? ')
    print(f'Nome: {nome}\nTempo de casamento: {tempo} anos')
else:
    print(f'Nome: {nome}\nObrigado e até a próxima')
