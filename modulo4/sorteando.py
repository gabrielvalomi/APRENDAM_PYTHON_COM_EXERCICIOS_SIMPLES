from random import randint

def sorteio(lista):
    for c in range(0, 10):
        n = randint(1, 20)
        lista.append(n)
        print(f'o valor sorteado foi {c}')

def soma(lista):
    soma =0 
    for valor in lista:
        valor % 2 == 0
        soma = soma + valor
        print(f'a soma dos valores foi {valor}')

numero = list()
sorteio(numero)
soma(numero)


    

