from datetime import date
atual = date.today ().year
nascimento = int(input('ano de nacimento: '))
idade = atual - nascimento
print('o atleta tem {} anos.'.format(idade))
if idade<= 9:
    print('classificação: mirim')
elif idade >= 9 and idade < 18:
    print('clacificação: junior')
elif idade >= 18:
    print('classificação: adulto')

