for contador in range(1,51):
    if contador % 3 == 0:
        print(f'Número {contador}: FIZZ')

    elif contador % 5 == 0:
        print(f'Número {contador}: BUZZ')

    elif contador % 5 == 0 and contador % 3 == 0:
        print(f'Número {contador}: FIZZBUZZ')
    
    else:
        print(f'Número: {contador}')