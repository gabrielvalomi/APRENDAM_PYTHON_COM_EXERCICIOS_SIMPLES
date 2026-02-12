numeros = (1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20)
pessoa = int(input('digite um numero de 0 a 12 : '))
for c in range(1, pessoa):
    print(c)

#ou
while True:
    numeros = int(input('digite um numero entre 0 e 20: '))
    if 0<= numeros <=20:
            break
    print('tente novamenre')