r1 = int(input('digite a primeira medida: '))
r2 = int(input('digite a primeira medida: '))
r3 = int(input('digite a primeira medida: '))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('os si=egmentos acima podem formar um triangulo')
if r1 == r2 ==r3:
    print('equilatero')
elif r1 != r2 != r3 != r1:
     print('escaleno')
else:
    print('isoceles')