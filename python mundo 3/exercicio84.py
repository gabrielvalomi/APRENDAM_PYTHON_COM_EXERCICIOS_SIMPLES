galera = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('qual e seu nome: ')))
    dados.append(int(input('qual e seu peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    p = str(input('quer continuar[s/n]: '))
    if p in 'Nn':
        break
print()
print(f' os dados coletados foram {galera}')
print()
print(f'no tiotal foram {len(galera)} cadastradas')
print()
print(f'o maior peso foi de {mai} kg de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}', end='')
    if p[1] == men:
        print(f'{p[0]}')
print(f'o menor peso foi de {men} kg')

