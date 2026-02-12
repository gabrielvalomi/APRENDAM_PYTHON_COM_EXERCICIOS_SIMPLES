num = 0
cont = 0
soma = 0
num = num = int(input('digite um numero [999 para parar]: '))
while num !=999:
    soma =soma + num 
    cont = cont + 1
    num = int(input('digite um numero [999 para parar]: '))
print('voce digitou {} numeros e a soma entre eles doi {}'.format(cont, soma))