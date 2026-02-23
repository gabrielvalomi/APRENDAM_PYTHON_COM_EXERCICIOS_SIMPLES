def voto(ano):
    from datetime import date
    atual = date.todey().year
    idade = atual - ano
    if idade <=16:
        return f'voce esta apito a votar com a idade de {idade}'
    elif 16<= idade < 18 or idade > 65:
        return f' voce pode ter a opição de votar ou nao votar com a idade de {idade}'
    else:
        return f'voce ja pode votar com a idade de {idade}'

nasc = int(input('em que ano voce nasceu:  '))
print(voto(nasc))



