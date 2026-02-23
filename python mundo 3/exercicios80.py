lista = []
for c in range(0,5):
    n = int(input(' digite seu valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
for i, v in enumerate(lista):
    print(f'voce digitou {v} valores')
print('-='* 30)
lista.sort(reverse=True)
print(f'os numeros em ordem decrecente fotam{lista}')
print('-='*30)
print(f'o valor {lista[3]} faz parte da lista')
print('-='*30)
print(f'os valores add são {lista}')

