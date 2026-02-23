#faça um programa que leia o ano de nascimento de um jovem e informe de acordo comm sua idade. se ele ainda vai se alistar ao serviço militar.
from datetime import date
atual = date.today().year
sexo = str(input('digite seu sexo: '))
nacimento = int(input('digite seu ano de nacimento: '))
sexo1 = 'F'
sexo2 = 'M'
idade = atual - nacimento
print('se vc for {} se não sera dispensada, quem naceu em {} tem {} anos em {}'.format(sexo1, sexo2, nacimento, idade, atual))
if sexo == 'masculino' :
    print(' continue avançando')
else:
    print( 'voce esta dispensada ')
if idade == 18:
    print('voce deve ser alistar imediatamente')
elif idade > 18:
    saldo = idade - 18
    print(' voce ja esta alistado, se nao tiver servido deve comparecer a uma junta militar imeditamente'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print(' voce ainda não tem 18 anos, ainda faltam {} anos para servir'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))
