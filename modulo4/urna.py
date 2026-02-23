lula= []
bolsonaro = []
while True:
    voto = int(input('digite seu voto: '))
    if voto == 13:
        lula.append(13)
    elif voto == 22:
        bolsonaro.append(22)
    elif voto == 0:
        break
    else:
        print('voto invalido')
print(f'Lula teve {len(lula)} votos')
print(f'Bolsonaro teve {len(bolsonaro)} votos')