num = list()
pares = list()
inpar = list()
while True:
    num.append(int(input('digite um numero:')))
    pergunta = str(input('quer continuar[s/n]: '))
    if pergunta in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        inpar.append(v)
print()
print(f'a lista completa e {num}')
print()
print(f' esses são os numeros pares{pares}')
print()
print(f'os valores impares {inpar}')