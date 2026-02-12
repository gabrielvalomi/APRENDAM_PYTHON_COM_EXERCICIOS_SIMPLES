from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opçoes:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('qual sua jogada? '))
print('jo')
print('ken')
print('po!!!')
print('-=' * 11)
print('computador jogou{}'.format(itens[computador]))
print('jogador jogou{}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('jogador ganhor')
    else:
        print('jogada invalida')
elif computador == 1:
    if jogador == 0:
        print ('jogador ganhou')
    elif jogador == 1:
        print('empatou')
    elif jogador == 2:
        print('jogador ganhou')
    else:
        print('jogada invalida')

elif computador == 2:
    if jogador == 0:
        print('jogador ganhou')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida')