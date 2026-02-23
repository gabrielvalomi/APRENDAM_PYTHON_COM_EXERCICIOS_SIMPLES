lista =[]
while True:
    lista.append(int(input(' difite um valor:')))
    p = 'quer continuar [s/n]: '
    if p in 'Nn':
        break
print('-='* 30)
print(f' voce difitou')