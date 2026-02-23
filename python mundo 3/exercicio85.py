valores = []
pares = []
impar =[]
for c in range(0, 6):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 ==1:
        impar.append(n)
    valores.append(pares[:])
    valores.append(impar[:])
print(f'o valores digitados foram { valores}')
print(f'os valores pares foram {pares}')
print(f' os valores impares foram {impar}')

#ou
valores = [[], []]
valor = 0
for c in range(0, 6):
    valor = int(input('digite um valoe: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    elif valor % 2 == 1:
        valores[1].append(valor)
print(f'o valores digitados foram { valores}')
print(f'os valores pares foram {valores[0]}')
print(f' os valores impares foram {valores[1]}')

