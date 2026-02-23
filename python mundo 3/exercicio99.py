from time import sleep

def analize(*num):
    cont = 0
    maior = 0
    print(' analizando os valores passados...')
    for valor in num:
        print(f'{valor}', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
print(f'os valores informados foram{analize}')
print('o maior valor foi{maior}')




analize(1, 2, 4, 5, 8, 10, 22 )
analize(22, 43, 2, 7, 4, )
analize(2, 8, 5, 3, 1 )