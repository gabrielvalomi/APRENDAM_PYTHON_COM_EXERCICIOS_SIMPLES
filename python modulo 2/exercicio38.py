#escreva um programa que meia dois numeros inteiros e compare-os mostrando qual valor e maior ou igual
n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
if n1 > n2:
    print('primeiro numero e maior ')
elif n2 > n1:
    print('segundo numero e maior')
elif n1 == n2:
    print('os numeros são igauis')
else:
    print('o numero e invalido')
