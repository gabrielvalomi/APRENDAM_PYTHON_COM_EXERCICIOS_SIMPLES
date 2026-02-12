primeiro = int(input('digite seu numero: '))
razão = int(input('razão: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} -'.format(termo), end= '')
    termo = termo + razão
    cont = cont + 1
print('fim')

