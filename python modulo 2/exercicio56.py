somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulherescomw20 = 0
for pessoa in range(1, 5):
    print('-----pessoa {}-----'.format(pessoa))
    nome = str(input('qual seu nome: ')).strip()
    idade = int(input('qual sua idade: '))
    sexo = str(input('qual o seu sexo: '))
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'M':
        maioridadehomem = idade 
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'F' and idade <= 20:
        mulherescomw20 = mulherescomw20 + 1

mediaidade = somaidade / 4
print(' a media de idade e igual {}'.format(mediaidade))
print(' o homem mais veho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('temos {} com menos de 20 anos'.format(mulherescomw20))