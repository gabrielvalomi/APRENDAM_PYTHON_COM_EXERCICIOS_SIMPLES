maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('qual e seu peso:{} '.format(pess)))
    if pess == 1:
        maior = pess
        menor = pess
        print('este peso foi o maior de todos')
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso é{}'.format(maior))
print(' o menor peso é{}'.format(menor))

    