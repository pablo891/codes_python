animais = ['Cachorro', 'Gato', 'Ovelha']
print(type(animais)) # Exibindo o tipo de variável

print(animais)

# Exibindo todos os itens da lista
print('-' * 50)
for itens in animais:
    print(itens)
# ---------------------------------------------------------------------------------------------
# 1ª Etapa: Atualizar dados (Update)

print('-' * 50)
animais[0] = 'Coelho'
print(animais)

# ---------------------------------------------------------------------------------------------
# 2ª Etapa: Inserir dados (Create)

print('-' * 50)
# forma 1 - Usando append
animais.append('Cavalo') # irá inserir um novo item ao final da lista
print(animais)

#forma 2 - Usando insert
animais.insert(1, 'Pássaro') #O insert precisa de 2 valores, o 1º será o índice que deseja inserir o valor, o 2º é o conteúdo que quero inserir na linha
print(animais)

# ----------------------------------------------------------------------------------------------
#3ª Etapa: Excluir dados (Delete)

print('-' * 50)
# forma 1 - usando pop()
animais.pop() # Remove o último item da lista
print(animais)
# forma 2 - usando pop() com índice
animais.pop(0) # Aqui iremos escolher qual índice da lista será excluído
print(animais)
# forma 3 - usando remove
animais.remove('Ovelha') # irá remover o item pelo seu conteúdo
print(animais)