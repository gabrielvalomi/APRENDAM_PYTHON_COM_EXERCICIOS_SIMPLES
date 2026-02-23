valores = list()
min = 0
mai = 0
cont = 0
while cont in range(0, 6):
    valores.append(int(input('digite um numero: ')))
    cont = cont + 1
    if cont == 0:
        min = mai = valores[cont]
    else:
        if valores[cont] > mai:
            mai =valores[cont]
        if valores[cont] < min:
            min = valores[cont]
print(f' voce digitou os valores {valores}')
print(f'o numero maximo foi {max} na posição ')
for i, v  in enumerate(valores):
    if v == mai:
        print(f'{i}....', end='')
print()
print(f' o valor minimo e de {min} na posição ')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}....', end='')
print()


