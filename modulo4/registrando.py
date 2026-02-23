cadastro = str(input('voce possui um cadastro[S/N]: '))
lista = [[], [], []]


while True:
    if cadastro in 'Nn':
        emial = str(input('digite seu email: '))
        nameuser= str(input('digite seu nome de usuer: '))
        print('senha deve conter caracteres especificos como @,#')
        senha =int(input('digite sua senha: '))
        lista[0].append(emial)
        lista[1].append(nameuser)
        lista[2].append(senha)
    if cadastro in 'Ss':
        nameuser = str(input('digite sua seu nome de usuario: '))
        if nameuser not in lista:
            print('usuario nao cadastrado, por favor digite um nome de usuario valido')
        nameuser = str(input('digite sua seu nome de usuario: '))
        senha = int(input('digite sua senha: '))
    else:
        break
print(lista)



