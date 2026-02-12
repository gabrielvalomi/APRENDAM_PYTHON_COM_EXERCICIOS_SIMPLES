nota1 = float(input('digite sua nota: '))
nota2 = float(input('digite sua nota: '))
media = (nota1 + nota2) / 2
print('se sua nota 1 é{:.1f},  sua nota2 é{:.1f}, sua media sera{:.1f}'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('voce esta em recuperação')
elif media >= 8:
    print('voce esta aprovado')