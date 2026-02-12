casa = float(input('valor da casa: R'))
salário = float(input('salario do comprador: r$'))
anos = int(input('quantos anos de financiamneto?'))
prestação = casa / (anos * 12)
minimo = salário *30/100
print('para pagar uma casa de r${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de {:.2f}'.format(prestação))

print('COMPARANDO tem que pagar {} e o minimo e de {}'.format(prestação, minimo))
if prestação <= minimo:
    print('emprestimo aprovado')
else:
    print('emprestimo negado')