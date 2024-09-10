age = int(input('Digite o ano: '))

if age % 400 == 0:
    print(f'O ano {age} é bissexto')
elif age % 4 == 0 and age % 100 != 0:
    print(f'O ano {age} é bissexto')
else:
    print(f'O ano {age} não é bissexto')
