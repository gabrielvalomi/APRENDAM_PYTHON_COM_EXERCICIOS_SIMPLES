listagem = ('lapis', 1.80,
           'borracha', 2.0,
           'caderno', 15.75,
           'estojo', 25,
           'compasso', 9.99)
print('-='* 20)
print('listagem de preço:^40')
print('-='* 20)
for item in range(0, len(listagem)):
    if item % 2 ==0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')

