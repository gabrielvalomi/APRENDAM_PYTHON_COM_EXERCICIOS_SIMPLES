n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
print(''''digite
[1]para soma
[2]para subtração
[3]para muntiplicação 
[4]para divisão''')
conta = int(input('qual e a conta: '))
while conta == 0:
    if conta == 1:
        resultado = n1 + n2
        print('a soma entre {} e {} e igual a {}'.format(n1, n2, resultado))
    elif conta == 2:
        resultado = n1 - n2
        print('a subtração entre {} e {} e igual a {}'.format(n1, n2, resultado))
    elif conta == 3:
        resultado = n1 * n2
        print('a multiplicação entre {} e {} e igual a {}'.format(n1, n2, resultado))
    elif conta == 4:
        resultado = n1 / n2
        print('a divisão entre {} e {} e igual a {}'.format(n1, n2, resultado))


