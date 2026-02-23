from time import sleep
a = int(input('digite um numeor: '))
b = int(input('digite um numeor: '))
c = int(input('digite um numeor: '))

def contador(a, b, c):
    print(f'contagem de {a} ate{b} em {c}')

if a <= b :
    cont = a
    while cont <= b:
        print(f'{cont}', end='')
        sleep(0.5)
        cont = cont + c
else:
    cont = a
    while cont >= b :
        print(f'{cont}', end='')
        sleep(0.5)
        cont = cont - b





