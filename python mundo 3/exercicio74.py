from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
      randint(1, 10) )
print('os valor sorteados foram: ', end='')
for n in numero:
    print(f'{n}', end='')

print(f'\n o maior valor sorteado foi {max(numero)}')
print(f' o menor valor sorteado foi {min(numero)}')
