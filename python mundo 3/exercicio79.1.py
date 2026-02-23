lista = list()
while  True:
    n =(int(input('digite seu numero: ')))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso')
    else:
        print('este numero ja esta em uso')
    pergunta = str(input(' quer continuar [S/N]: '))
    if pergunta in 'Nn':
        break
print(' voce solicitou nao continuar')
lista.sort()
print(f'voce adicionol os valores {lista}')
