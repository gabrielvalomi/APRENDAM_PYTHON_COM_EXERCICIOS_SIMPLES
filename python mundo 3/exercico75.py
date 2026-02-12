numeros = ( int(input('digite um valor:')),
            int(input('digite um valor:')),
              int(input('digite um valor:')),
              int(input('digite um valor:')))
print(f' voce digitou os valores{numeros}')
print(f'o valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f' o valor 3 apareceu {numeros.index(3)} posição')
else:
    print('o numero 3 nao foi digitado')
for n in numeros:
    if n % 2 == 0:
        print(f'os numros{n} são pares ')

 