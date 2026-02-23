valores = list()
cont = 0
while cont in range(0, 5):
    valores.append(int(input('difite um valor: ')))
    cont = cont + 1
print(f'o maior valor foi {max(valores)}')
print(f'o menor valor foi {min(valores)}')
print(f'o valor {max(valores)} esta na posição')
print(valores)