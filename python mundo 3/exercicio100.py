from random import randint


def sortea(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'os valores sorteados foram{cont}')


def somapar(lista):
    soma = 0 
    for valor in lista:
        if valor % 2 ==0:
            soma = soma + valor
    print(f'o resultado das somas foi {valor}')

numeros = list()
sortea(numeros)
print(numeros)



