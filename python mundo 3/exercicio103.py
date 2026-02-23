def ficha(jog='<desconhecido>', gol=0):
    print(f'o jogador {jog} fez {gol} na copa')
    return jog, gol

nome = str(input('nome do jogador: '))
gols = str(input('numeros de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() =='':
    ficha(gol = gols)
else:
    ficha(jog=nome, gol = gols)