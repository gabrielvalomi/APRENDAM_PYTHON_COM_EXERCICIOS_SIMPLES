galera =[]
dado =[]
for p in range(0, 3):
    dado.append(str(input('digite seu nome: ')))
    dado.append(int(input('digite sua idade: ')))
    galera.append(dado[:])
print(galera)
